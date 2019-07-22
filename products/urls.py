from django.conf.urls import url

from .views import (
	ProductListView, 
	product_list_view, 
	product_detail_view,
	product_detail_slug_view,
	ProductDetailSlugView,
	# ProductFeaturedListView,
	# ProductFeaturedDetailView,

)	

urlpatterns = [

    # url(r'^products/$',ProductListView.as_view(), name="list"),
    url(r'^products/$',product_list_view, name="list"),
    # url(r'^products/(?P<pk>\d+)/$', product_detail_view),
    # url(r'^products/(?P<pk>\d+)/$', ProductDetailView.as_view(), name='detail'),
    url(r'^products/(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),
    url(r'^products/(?P<slug>[\w-]+)/$', product_detail_slug_view, name='detail'),

     # url(r'^featured/$',ProductFeaturedListView.as_view()),
     # url(r'^featured/(?P<pk>\d+)$',ProductFeaturedDetailView.as_view()),

]
