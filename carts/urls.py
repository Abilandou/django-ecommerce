from django.conf.urls import url

from .views import (
	cart_home,
	cart_update,
	checkout_home,
	checkout_done_view,
	success_payment_view,
	failure_payment_view,
	remove_from_cart
)

urlpatterns = [
		url(r'^$', cart_home, name="cart_home"),
		url(r'^update/$', cart_update, name='update'),
		url(r'^checkout/$', checkout_home, name="checkout"),
		url(r'^checkout/success/$', checkout_done_view, name="success"),
		url(r'^checkout/success_payment/$', success_payment_view, name="payment_success"),
		url(r'^checkout/failure_payment/$', failure_payment_view, name="payment_failure"),
		url(r'^delete_product/(?P<pk>\d+)/$', remove_from_cart, name='remove')

		# url(r'^(?P<object_id>[0-9]+)/delete_answer/$', views.objectDelete, name='delete_object')
		# url(r'^del_product/(?P<pk>\d+)/$', remove_from_cart, name="del")
]

