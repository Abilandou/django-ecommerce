import random
import string

from django.utils.text import slugify

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))


def unique_order_id_generator(instance):
	"""This slug can be generated for models assumed to have a 
		slug field and a title field
	"""
	order_new_id = random_string_generator()

	klass = instance.__class__
	qs_exists = klass.objects.filter(order_id=order_new_id).exists()
	if qs_exists:
		return unique_slug_generator(instance)
	return order_new_id






def unique_slug_generator(instance, new_slug=None):
	"""This slug can be generated for models assumed to have a 
		slug field and a title field
	"""
	if new_slug is not None:
		slug = new_slug
	else:
		slug = slugify(instance.title)

	klass = instance.__class__
	qs_exists = klass.objects.filter(slug=slug).exists()
	if qs_exists:
		new_slug = "{slug}-{randstr}".format(
					slug=slug,
					randstr=random_string_generator(size=4)
			)
		return unique_slug_generator(instance, new_slug=new_slug)
	return slug

