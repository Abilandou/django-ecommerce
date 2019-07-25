
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, get_user_model
from django.utils.http import is_safe_url

from .models import GuestEmail

from .forms import LoginForm, RegisterForm, GuestForm
from products.models import Product

from categories.models import Category

def guest_register_view(request):
    form = GuestForm(request.POST or None)
    context = {
        "form": form
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None

    if form.is_valid():
        email = form.cleaned_data.get("email")
        new_guest_email = GuestEmail.objects.create(email=email)
        request.session['guest_email_id'] = new_guest_email.id
        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect("/register/")

    return redirect("/register/")


def login_page(request):
    categories = Category.objects.all()
    form = LoginForm(request.POST or None)
    context = {
        "title": "Login To Your Account",
        "form": form,
        "categories": categories,
    }
    # print(request.user.is_authenticated())
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None

    if form.is_valid():
        # print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        # print("User Logged in")
        user = authenticate(request, username=username, password=password)
        # print(request.user.is_authenticated())

        if user is not None:
            # print(request.user.is_authenticated())
            login(request, user)
            try:
                del request.session['guest_email_id']
            except:
                pass
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect('/cart/')
        else:
            # return an invalid message
            print("Error");
          
    return render(request, "accounts/login.html", context, {} )


User = get_user_model()


def register_page(request):
    categories = Category.objects.all()
    form = RegisterForm(request.POST or None)
    context = {
        "title": "New User Register",
        "form": form,
        "categories": categories,
    }
    if form.is_valid():
        print(form.cleaned_data)
        name = form.cleaned_data.get("name")
        email = form.cleaned_data.get("email")
        username = form.cleaned_data.get("username")
        new_user = User.objects.create_user(name, email, username)
        return redirect("/login")

        # print(new_user)

    return render(request, "accounts/register.html", context, {})
