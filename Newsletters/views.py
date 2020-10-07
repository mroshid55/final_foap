from django.shortcuts import render, get_object_or_404, redirect

#--message--#
from django.contrib import messages
#--model--#
from .models import *
#--model import Home_Page --#
from Home_Page.models import *
#--Import Form--#
from .form import *

#--Email Start--#

# Email sender django
from django.core.mail import EmailMessage
# EMAIL_HOST_USER call from settings
from django.conf import settings
# Call from template mail_temp.html
from django.template.loader import render_to_string

#--Email End--#


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
                #--Email setting Start--#

                #--cleaned_data from RegistrationForm--#

                Email_Name = form.cleaned_data['Email']

                #--cleaned_data from RegistrationForm--#

                template = render_to_string('newsletters/mail_sign.html')
                email = EmailMessage(
                    'Thanks for Subscribing', template, settings.EMAIL_HOST_USER, [Email_Name],)
                email.fail_silently = False
                email.send()
                #--Email setting End--#

                return redirect('SignUp_Message')
        else:
            form = NewsletterSignUpForm()

    return render(request, 'newsletters/signup.html', {'cont': cont, 'logo': logo, 'form': form, 'slink': slink})


def success_message_newsletters(request):
    return render(request, 'newsletters/signup_success.html')
