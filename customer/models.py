from django.db import models
from goods.models import *


class Customer(models.Model):

	email = models.EmailField(blank=True)
	phone = models.CharField(max_length=125, null=True, blank= True)
	registration_date = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)

	def __unicode__(self):
		return '%s %s' % (self.email, self.phone)


class Order(models.Model):

	customer = models.ForeignKey(Customer)
	good = models.ManyToManyField(Good)
	order_date = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)

	def __unicode__(self):
		return '%s' % self.customer



