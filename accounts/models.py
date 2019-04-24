from django.db import models

# Create your models here.

class GuestEmail(models.Model):
	email 		= models.EmailField(null=True, default='guest_email')
	name		= models.CharField(null=True, default='guest', max_length=120)
	active 		= models.BooleanField(default=True)
	update		= models.DateTimeField(auto_now=True)
	timestamp	= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name