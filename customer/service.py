from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.shortcuts import render_to_response, RequestContext, get_object_or_404




def service(request):

	customer_service="Customer Service"

	
	return render_to_response('services.html', locals(), context_instance=RequestContext(request))
