from django.views.generic import ListView, DetailView

from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Product

from carts.models import Cart


# class ProductFeaturedListView(ListView):
# 	template_name = "products/list.html"

# 	def get_queryset(self, *args, **kwargs):
# 		request = self.request
# 		return Product.objects.featured()


class ProductFeaturedDetailView(DetailView):
	template_name = "products/featured-detail.html"

	def get_queryset(self, *args, **kwargs):
		request = self.request     
		return Product.objects.featured()

	def context_data(self, *args, **kwargs):
		context = super(product_detail_slug_view, self).get_context_data(*args, **kwargs)
		cart_obj, new_obj = Cart.objects.new_or_get(self.request)
		context['cart'] = cart_obj
		# print(cart_obj)
		return context


class ProductListView(ListView):
	queryset = Product.objects.all()
	template_name = "product/product_list.html"

	def get_context_data(self, *args, **kwargs):
		context = super(ProductListView, self).get_context_data(*args, **kwargs)
		print(context)
		return context


def product_list_view(request):
	queryset = Product.objects.all()#List all products in database
	context = {
		'title': 'Listing all Products',
		'allProducts': queryset
	}

	return render(request, "product/product_list.html", context)


class ProductDetailView(DetailView):
	queryset = Product.objects.all()
	template_name = "product/product_detail.html"

	def get_context_data(self, *args, **kwargs):
		context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
		print(context)
		return context

	def get_object(self, *args, **kwargs):
		request = self.request
		pk = self.kwargs.get('pk')
		instance = Product.objects.get_by_id(pk)
		if instance is None:
			raise Http404("Product deosn't exists")
		return instance

	def get_queryset(self, *args, **kwargs):
		request = self.request
		pk = self.kwargs.get('pk')
		return Product.objects.filter(pk=pk)


def product_detail_view(request, pk=None, *args, **kwargs):
	# getSingleProduct = Product.objects.get(pk=pk)#pk=id
	# getSingleProduct = get_object_or_404(Product, pk=pk)
	# instance = Product.objects.filter(id=pk)
	# print qs
	instance = Product.objects.get_by_id(pk)
	if instance is None:
		raise Http404("Product doesn't exists")
	# if qs.exists() and qs.count() ==1:#len(qs)
	# 	instance = qs.first()
	# else:
	# 	raise Http404("Product doesn't exists")
	context = {
		'title': 'Product Detail',
		'productDetail': instance
	}

	return render(request, "product/product_detail.html", context, {})


class ProductDetailSlugView(DetailView):
	queryset = Product.objects.all()
	template_name = "product/product_detail.html"

	def context_data(self, *args, **kwargs):
		context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
		cart_obj, new_obj = Cart.objects.new_or_get(self.request)
		context['cart'] = cart_obj
		# print(cart_obj)
		return context 

	# def get_object(self, *args, **kwargs):
	# 	request =self.request
	# 	slug = self.kwargs.get(slug)

	# 	try:
	# 		instance = Product.objects.get(slug=slug, published=True)
	# 	except Product.DoesNotExist:
	# 		raise Http404("Product Not Found...")
	# 	except Product.MultipleObjectsReturned:
	# 		qs = Product.objects.filter(slug=slug, published=True)
	# 		instance = qs.first()
	# 	except:
	# 		raise Http404("This is strange")

	# 	return instance


def product_detail_slug_view(request, slug=None, *args, **kwargs):

	getAllProductsInCart = Cart.objects.all()
	getSingleProduct = get_object_or_404(Product, slug=slug)
	context = {
		'title': 'Product Detail',
		'productDetail': getSingleProduct,
		'allCarts':getAllProductsInCart
	}

	# def context_data(self, *args, **kwargs):
	# 	context = super(product_detail_slug_view, self).get_context_data(*args, **kwargs)
	# 	cart_obj, new_obj = Cart.objects.new_or_get(self.request)
	# 	context['cart'] = cart_obj
	# 	print(cart_obj)
	# 	return context

	return render(request, "product/product_detail.html", context, {})
