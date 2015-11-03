from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.shortcuts import render_to_response, RequestContext, get_object_or_404
from goods.models import Good, Photo


def all_products(request):
	images = Photo.objects.all()

	'''__gt filter object with price > 20 
	'https://docs.djangoproject.com/en/1.8/topics/db/queries/'''
	# products = Good.objects.filter(price__gt=20)
	products = Good.objects.filter(active=True)
	# context = {
	# 	'products':products
	# } 
	# products = Good.objects.all(price)
	# photo = Photo.objects.filter(product__name="phone")
	# all_photos = products.photo_set.all()
		
	# return render(request,'all_products.html', context) #### possible variant
	return render_to_response('all_products.html', locals(), context_instance=RequestContext(request))

def single_product(request, slug):
	# s_product = get_object_or_404(Good, slug=slug)

	s_product = Good.objects.filter(slug=slug)
	# context = {
	# 	's_product':s_product
	# }
	# return render(request,'single_product.html', context, slug)
	return render_to_response('single_product.html', locals(), context_instance=RequestContext(request))

    






# def product(request):
	
# 	template = 'index.html'
# 	context = {}
# 	return render (request, 'index.html', context)

# 	# return HttpResponse( 'index.html', context )
