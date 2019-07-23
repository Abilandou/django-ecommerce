from django.conf.urls import url

from .views import (
	categories_list,
    category_detail_view

)

urlpatterns = [

    url(r'^categories/$',categories_list, name="cats"),
    url(r'^categories/(?P<name>[\w-]+)/$', category_detail_view, name='detail'),


]
