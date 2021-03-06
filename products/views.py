from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Product

from carts.models import Cart
from categories.models import Category


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


def product_list_view(request, category_name=None):
	category = None
	products_list = Product.objects.all()  # List all products in database
	page = request.GET.get('page', 1)

	paginator = Paginator(products_list, 3)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)

	categories = Category.objects.all()
	if category_name:
		category = get_object_or_404(Category, slug=category_name)
		products = Product.filter(category=category)
	context = {
		'title': 'Listing all Products',
		'allProducts': queryset,
		'categories': categories,
		'category': category,

	}

	return render(request, "product/product_list.html", context)


class ProductDetailView(DetailView):
	queryset = Product.objects.all()
	categories = Category.objects.all()
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

	instance = Product.objects.get_by_id(pk)
	categories = Category.objects.all()
	if instance is None:
		raise Http404("Product doesn't exists")

	context = {
		'title': 'Product Detail',
		'productDetail': instance,
		'categories': categories,
	}

	return render(request, "product/product_detail.html", context, {})


class ProductDetailSlugView(DetailView):
	queryset = Product.objects.all()
	categories = Category.objects.all()
	template_name = "product/product_detail.html"

	def context_data(self, *args, **kwargs):
		context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
		cart_obj, new_obj = Cart.objects.new_or_get(self.request)
		context['cart'] = cart_obj
		# print(cart_obj)
		return context 


def product_detail_slug_view(request, slug=None, *args, **kwargs):
	categories = Category.objects.all()
	getAllProductsInCart = Cart.objects.all()
	getSingleProduct = get_object_or_404(Product, slug=slug)
	context = {
		'title': 'Product Detail',
		'productDetail': getSingleProduct,
		'allCarts':getAllProductsInCart,
		'categories': categories,
	}

	return render(request, "product/product_detail.html", context, {})
