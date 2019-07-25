"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

#----------------Static files configuration........................
from django.conf import settings
from django.conf.urls.static import static

#..................end static files configuration.................


#imported urls from other apps

from products.urls import urlpatterns
from search.urls import urlpatterns
from carts.urls import urlpatterns

#......End........

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import LogoutView

from django.views.generic import TemplateView

from accounts.views import(      
    login_page, 
    register_page,
    guest_register_view
)

from .views import(
     home_page, 
     contact_page, 
     service_page, 
)

from addresses.views import (
    checkout_address_create_view,
    checkout_address_reuse_view,
)


urlpatterns = [
#Main pages

    url(r'^$', home_page, name="home"),
    url(r'^contact/$', contact_page, name="contact"),
    url(r'^service/$', service_page),
    url(r'^bootstrap/$', TemplateView.as_view(template_name="bootstrap/bootstrap_example.html")),
    url(r'^register/$', register_page, name="register"),
    url(r'^login/$', login_page, name="login"),
    url(r'^checkout/address/create/$', checkout_address_create_view, name="checkout_address_create"),
    url(r'^checkout/address/reuse/$', checkout_address_reuse_view, name="checkout_address_reuse"),
    url(r'^register/guest/$', guest_register_view, name="guest_register"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),

    # Included urls

    url(r'^', include('products.urls', namespace="products")),
    url(r'^search/', include('search.urls', namespace="search")),
    url(r'^cart/', include('carts.urls', namespace="cart")),
    url(r'^', include('categories.urls', namespace="categories")),
    url('paypal/', include('paypal.standard.ipn.urls', namespace="paypal")),

    # End included url

    # Admin Register Routes
    url(r'^admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
