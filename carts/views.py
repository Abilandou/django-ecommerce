from django.shortcuts import render, redirect, get_object_or_404

from .models import Cart
from orders.models import Order
from accounts.forms import LoginForm, GuestForm
from billing.models import BillingProfile
from accounts.models import GuestEmail
from addresses.forms import AddressForm
from addresses.models import Address
from products.models import Product
from categories.models import Category


def cart_home(request):
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	# print(cart_obj)
	
	products = cart_obj.products.all()
	categories = Category.objects.all()

	total = 0
	for cartItem in products:
		total += cartItem.price
	# print(total) 
	cart_obj.total = total
	cart_obj.save()
	
	return render(request, "carts/cart_home.html", {"cart": cart_obj, 'categories': categories})


def cart_update(request):
	print(request.POST)
	product_id = request.POST.get('product_id')
	if product_id is not None:
		try:
			product_obj = Product.objects.get(id=product_id)
		except Product.DoesNotExist:
			print("The product you request for does not exists")
			return redirect("cart:cart_home")
		cart_obj, new_obj = Cart.objects.new_or_get(request)
		# cart_obj.products.add(product_obj)
		if product_obj in cart_obj.products.all():
			cart_obj.products.remove(product_obj)

		else:
			cart_obj.products.add(product_obj)
		request.session['cart_items'] = cart_obj.products.count()
	
	return redirect("cart:cart_home")


def remove_from_cart(request, product_id=None):
	pass


def checkout_home(request):
	cart_obj, cart_created = Cart.objects.new_or_get(request)
	order_obj = None
	if cart_created or cart_obj.products.count() == 0:
		return redirect("cart:cart_home")
		
	login_form 			 =  LoginForm()
	guest_form 			 =  GuestForm()
	address_form 		 =  AddressForm()
	# billing_form 		 = AddressForm()
	billing_address_id = request.session.get("billing_address_id", None)
	shipping_address_id = request.session.get("shipping_address_id", None)

	# Initial user address to None
	address_qs = None

	billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)

	if billing_profile is not None:

		if request.user.is_authenticated():
			# Get user address automatically on shipping and Billing form
			address_qs = Address.objects.filter(billing_profile=billing_profile)  # return user billing profile
		# else:
		# 	shipping_address_qs = address_qs.filter(address_type='shipping')# shipping address
		# 	billing_address_qs = address_qs.filter(address_type='billing')# billing address

		order_obj, order_obj_created = Order.objects.new_or_get(billing_profile, cart_obj)
		if shipping_address_id:
			order_obj.shipping_address = Address.objects.get(id=shipping_address_id)
			del request.session["shipping_address_id"]

		if billing_address_id:
			order_obj.billing_address = Address.objects.get(id=billing_address_id)
			del request.session["billing_address_id"]
		if billing_address_id or shipping_address_id:
			order_obj.save()

		if request.method == "POST":
			"verify order is done"
			is_done = order_obj.checkout_done()
			if is_done:
				order_obj.mark_paid()
				request.session['cart_items'] = 0
				del request.session['cart_id']
			order_obj.mark_paid()
			# del request.session['cart_id']
			return redirect("cart:success")

		'''
			update order_obj to done, "paid"
			del request.session['cart_id]
			redirect to success
		'''

	context = {
		"object": order_obj,
		"billing_profile": billing_profile,
		"login_form": login_form,
		"guest_form":guest_form,
		"address_form":address_form,
		# "billing_form":billing_form,
		"address_qs": address_qs  # user address added in context to seen in the view(html pages)
		# "shipping_address_qs": shipping_address_qs,
		# "billing_address_qs": billing_address_qs

	}
	return render(request, 'carts/checkout.html', context)


def checkout_done_view(request):
	return render(request, "carts/checkout_done.html", {})


def success_payment_view(request):
	return render(request, "carts/success_payment.html", {})


def failure_payment_view(request):
	return render(request, "carts/failure_payment.html", {})
