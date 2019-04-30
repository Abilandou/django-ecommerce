from django.db import models
import os
import random
from django.db.models import Q
from ecommerce.utils import unique_slug_generator
from django.db.models.signals import pre_save #This helps to generate the slug and its saved before the model saves

from django.urls import reverse

def get_filename_ext(filepath):
	base_name = os.path.basename(filepath)
	name, ext = os.path.splitext(base_name)
	return name, ext


def upload_image_path(instance, filename):
	# print(instance)
	# print(filename)
	new_filename = random.randint(1, 90990000)
	name, ext = get_filename_ext(filename)
	final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
	return "products/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)



class ProductQuerySet(models.query.QuerySet):
	def featured(self):
		return self.filter(featured=True)

	# def search(self, query):
	# 	lookups = Q(title__icontains=query) | Q(description__icontains=query)
	# 	return self.filter(lookups).distinct()

# # Overwriting the model default manager, objects

class ProductManager(models.Manager):
	def get_queryset(self):
		return ProductQuerySet(self.model, using=self._db)

	def featured(self):
		return self.get_queryset().filter(featured=True)
	# def all(self):
	# 	return self.get_queryset().published()

	def get_by_id(self, id):
		qs = self.get_queryset().filter(id=id) #Product.objects
		if qs.count() == 1:
			return qs.first()
		return None
	def search(self, query):
		return self.get_queryset().published().search(query)

PRODUCT_CATEGORIES = (
	('t-shirts', 'T-Shirts'),
	('shoes', 'Shoes'),
	('women wears', 'Women Wears'),
	('trousers', 'Trousers'),

)

class Product(models.Model):

	title            = models.CharField(max_length=120, unique=True)
	category         =  models.CharField(max_length=120, choices=PRODUCT_CATEGORIES, default="T-Shirt")
	slug             = models.SlugField(blank=True, unique=True)
	description      = models.TextField()
	price            = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
	image            = models.ImageField(upload_to=upload_image_path, null=True, blank=True, unique=True)
	featured         = models.BooleanField(default=False)
	published	     = models.BooleanField(default=True)
	timestamp        = models.DateTimeField(auto_now_add=True)

	#actually overwrite it by creating an instance
	#Not actually overwriting but extending to it.
	objects = ProductManager()

	def __str__(self):
		return self.title

	def name(self):
		return self.title

	#Get product detail urls
	def get_absolute_url(self):
		# return "/products/{slug}/".format(slug=self.slug)
		return reverse("products:detail", kwargs={"slug": self.slug} )
#Handle the pre save action
def product_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)