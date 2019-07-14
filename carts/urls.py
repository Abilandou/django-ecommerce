from django.conf.urls import url

from .views import (
	cart_home,
	cart_update,
	checkout_home,
	checkout_done_view,
	success_payment_view,
	failure_payment_view
)

urlpatterns = [
		url(r'^$', cart_home, name="cart_home"),
		url(r'^update/$', cart_update, name='update'),
		url(r'^checkout/$', checkout_home, name="checkout"),
		url(r'^checkout/success/$', checkout_done_view, name="success"),
		url(r'^checkout/success_payment/$', success_payment_view, name="payment_success"),
		url(r'^checkout/failure_payment/$', failure_payment_view, name="payment_failure")
		# url(r'^products/(?P<pk>\d+)/$', cart_update)
]

