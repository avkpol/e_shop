from django.shortcuts import render
from django.conf import settings
from django.views import generic
from django.core.mail import send_mail
from customer.forms import ContactForm


def contactUs(request):
    title = 'Contact Us'
    form = ContactForm(request.POST or None)
    confirm_message =None
    
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
            'confirm_message':confirm_message
        }
        
    # context = locals()
    template = 'contact.html'
    return render(request, template, context)


# Create your views here.
