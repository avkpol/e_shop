from django.contrib import admin


from .models import *

'''
makes custom model to reassign other models

'''

class PhotoInline (admin.TabularInline):

    model=Photo
    extra = 0

'''
reasign standart admin model
'''

class GoodAdmin (admin.ModelAdmin):
	inlines = [  PhotoInline ] #
	list_filter = ['name', 'price', 'available_q', 'add_date']
	list_display = ('name', 'price', 'available_q', 'add_date',)
	class Meta:
		model=Good

'''register Good as GoodAdmin'''

admin.site.register(Good, GoodAdmin) 


# admin.site.register(Good)
admin.site.register(Photo)