from django.shortcuts import render, get_object_or_404, redirect

#--message--#
from django.contrib import messages
#--model--#
from .models import *
#--model import Home_Page --#
from Home_Page.models import *
#--Import Form--#
from .form import *

# Create your views here.


def contact_info(request):

    cont = Contact.objects.all()  # Model Class Contact
    logo = Logo.objects.all()  # Model Class Logo
    slink = Social_link.objects.all()  # Model Class Social Link

    form = ContactForm(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():
            form.save(commit=False)
            form.save()
            messages.warning(
                request, 'Thank! your message has been sent successfully', 'alert alert-warning alert-dismissible')
        else:
            form = ContactForm()

    context = {'cont': cont, 'logo': logo, 'slink': slink, 'form': form}

    return render(request, 'contact/contactform.html', context)
