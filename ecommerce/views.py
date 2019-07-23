from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, get_user_model
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import ContactForm
from products.models import Product
from categories.models import Category


def nav_bar(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, "base/navbar.html", context,  {})


def home_page(request):
    print(request.session.get("firts_name", "Nothing"))
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
    context = {
        'title': "Welcome User",
        "content": "This is the home page let us get started",
        "featured_title":"Featured Products",
        "allProducts": queryset,
        'categories': categories,
        "premium_content": "You are also seeing this content because tou are logged in"
    }
    return render(request, "index.html", context,  {})


def service_page(request):
    return render(request, "service.html", {})


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    categories = Category.objects.all()
    context = {
        "title":"Contact",
        "content":"Wlecome to contact page.",
        "form": contact_form,
        'categories': categories,
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    # request.method = "POST"
    # print(request.POST.get('fullname'))
    # print(request.POST.get('email'))
    # print(request.POST.get('content'))
    return render(request, "allForms/contact/contact.html", context, {})



