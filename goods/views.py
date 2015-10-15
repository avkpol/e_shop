from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.shortcuts import render_to_response, RequestContext, get_object_or_404
from goods.models import Good

def all_products(request):
	images = Photo.objects.all()
    products = Good.objects.filter(active=True)
    photo = Photo.objects.filter(product__name="phone")
    prod = Good.objects.filter(price >100)
    all_photos = prod.photo_set.all()


    return render_to_response('all_products.html', locals(), context_instance=RequestContext(request))

    






# def product(request):
	
# 	template = 'index.html'
# 	context = {}
# 	return render (request, 'index.html', context)

# 	# return HttpResponse( 'index.html', context )
