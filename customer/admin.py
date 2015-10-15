from django.contrib import admin
from .models import *



class OrderInline (admin.TabularInline): # inline means including

    model=Order
    extra = 0



class CustomerAdmin (admin.ModelAdmin):
	inlines = [OrderInline ] 
	
	class Meta:
		model = Customer # Customer register in admin as CustomerAdmin 



admin.site.register(Customer, CustomerAdmin ) 
admin.site.register(Order) 