from django.shortcuts import render
from django.conf import settings
from django.views import generic
from django.core.mail import send_mail
from customer.forms import ContactForm
import datetime


def contactUs(request):

    title = 'Contact Us'
    form = ContactForm(request.POST or None)
    confirm_message =None
    now = datetime.datetime.now()


    if request.method == 'POST' and form.is_valid():
        comment = form.cleaned_data['comment']
        name = form.cleaned_data['last_name']
        subject = "thank you for your preorder"
        messages = '%s%s' %(comment, name)
        from_email = form.cleaned_data['email']
        to_us = [settings.EMAIL_HOST_USER]
        print subject, messages, from_email, to_us
        send_mail(subject, messages, from_email, to_us, fail_silently = True)
        title = "thank you"
        confirm_message = '''
        Thanks for your message. We will answer as soon as possible.
        '''
        form = None
    context = {
            
            'title': title,
            'form':form,
            'confirm_message':confirm_message,
            'now':now
      
        }
        
    # context = locals()
    template = 'contact.html'
    
    return render(request, template, context)

''' other way to render the same template with context'''

# from django.http import HttpResponse
# from django.template import loader, Context

# def contactUs(request):
#     now = datetime.datetime.now()
#     form = ContactForm()
#     template = loader.get_template('contact.html')
#     context = Context({'form':form,'now':now})
#     response = template.render(context)
    
    
#     return HttpResponse(response)


# Create your views here.
