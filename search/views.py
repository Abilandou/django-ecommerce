from django.shortcuts import render
from django.views.generic import ListView

from django.db.models import Q

from products.models import Product

from django.shortcuts import render


class SearchProductView(ListView):
	template_name = "search/items_searched.html"

	def get_context_data(self, *args, **kwargs):
		context = super(SearchProductView, self).get_context_data(*args, **kwargs)
		context['query'] = self.request.GET.get('q')
		return context

	def get_queryset(self, *args, **kwargs):
		request = self.request
		method_dict = request.GET
		query = method_dict.get('q', None)
		
		if query is not None:
			lookups = ( 
					Q(title__icontains=query) | 
					Q(description__icontains=query) |
					Q(tag__title__icontains=query)
				)
			return Product.objects.filter(title__icontains=lookups).distinct()
		return Product.objects.featured()