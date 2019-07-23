
# Create your views here.
from .models import Category
from products.models import Product


from django.shortcuts import render, get_object_or_404

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def categories_list(request):
    categories = Category.objects.all()

    page = request.GET.get('page', 1)
    # paginator = Paginator(query_Set, 20)
    # try:
    #     cat = paginator.page(page)
    # except PageNotAnInteger:
    #     cat = paginator.page(1)
    # except EmptyPage:
    #     cat = paginator.page(paginator.num_pages)
    return render(request, 'categories/categories.html', {'categories': categories})


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html', {'category': category, 'categories': categories, 'products': products})


def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug, available=True)
    category = product.category.filter(is_active=True)
    return render(request, 'shop/product/detail.html', {'product': product}, {'category': category})


def category_detail_view(request, name=None, *args, **kwargs):
    categories = Category.objects.all()
    category = get_object_or_404(Category, name=name)
    products = Product.objects.filter(category=category)

    # products_list = Product.objects.all()  # List all products in database
    page = request.GET.get('page', 1)

    paginator = Paginator(products, 2)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    return render(request, 'categories/category_detail.html', context={'category': category, 'allProducts': queryset, 'categories': categories})
