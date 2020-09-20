from django.shortcuts import render, get_object_or_404, redirect

#--message--#
from django.contrib import messages
#--model--#
from .models import *
#--model import Home_Page --#
from Home_Page.models import *
#--Import Form--#
from .form import *


def newslettersignup(request):

    cont = Contact.objects.all()  # Model Class Contact
    logo = Logo.objects.all()  # Model Class Logo
    slink = Social_link.objects.all()  # Model Class Social Link

    form = NewsletterSignUpForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            if NewsletterUser.objects.filter(Email=instance.Email).exists():
                messages.warning(
                    request, 'Your Email Already Exists In Our Database', 'alert alert-warning alert-dismissible')
            else:
                instance.save()
                return redirect('SignUp_Message')
        else:
            form = NewsletterSignUpForm()

    return render(request, 'newsletters/signup.html', {'cont': cont, 'logo': logo, 'form': form, 'slink': slink})


def success_message_newsletters(request):
    return render(request, 'newsletters/signup_success.html')
