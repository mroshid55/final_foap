from django.shortcuts import render, get_object_or_404, redirect

from django.core.paginator import Paginator
#--message--#
from django.contrib import messages
#--model--#
from .models import *
#--model import Home_Page --#
from Home_Page.models import *
#--Import Form--#
from .form import *

from .filters import *


#--Email Start--#

# Email sender django
from django.core.mail import EmailMessage
# EMAIL_HOST_USER call from settings
from django.conf import settings
# Call from template mail_temp.html
from django.template.loader import render_to_string

#--Email End--#

#--volunteer page--#


def volunteer(request):
    cont = Contact.objects.all()  # Model Class Contact
    logo = Logo.objects.all()  # Model Class Logo
    slink = Social_link.objects.all()  # Model Class Social Link
    Volun_teen = Volunteer.objects.all()
    return render(request, 'volunteer/join_in_volunteer.html', {'cont': cont, 'logo': logo, 'Volun_teen': Volun_teen, 'slink': slink})

###############################################################################################


def registration(request):
    cont = Contact.objects.all()  # Model Class Contact
    logo = Logo.objects.all()  # Model Class Logo
    slink = Social_link.objects.all()  # Model Class Social Link

    form = RegistrationForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            if Registration.objects.filter(Email=instance.Email).exists():
                messages.warning(request, 'Your Email Already Registered In Our Database, Please Try Another Email.',
                                 'alert alert-warning alert-dismissible')
            else:
                instance.save()
                #--Email setting Start--#

                #--cleaned_data from RegistrationForm--#

                Email_Name = form.cleaned_data['Email']
                F_Name = form.cleaned_data['Full_Name']
                #--cleaned_data from RegistrationForm--#
                template = render_to_string(
                    'volunteer/mail_temp.html', {'Name': F_Name})
                email = EmailMessage(
                    'Thanks For Registration', template, settings.EMAIL_HOST_USER, [Email_Name],)
                email.fail_silently = False
                email.send()
                #--Email setting End--#

                # #messages.success(request, 'Form Submission Successful')
                return redirect('Registration_Message')
        else:
            form = RegistrationForm()

    return render(request, 'volunteer/registration_form.html', {'cont': cont, 'logo': logo, 'form': form, 'slink': slink})

###############################################################################################


def registration_view(request):
    cont = Contact.objects.all()  # Model Class Contact
    logo = Logo.objects.all()  # Model Class Logo
    slink = Social_link.objects.all()  # Model Class Social Link
    reg_view = Registration.objects.all()
    myfilter = ProfileFilter(request.GET, queryset=reg_view)
    reg_view = myfilter.qs

    paginator = Paginator(reg_view, 10)
    page = request.GET.get('page')
    reg_view = paginator.get_page(page)

    context = {'cont': cont, 'logo': logo,
               'reg_view': reg_view, 'myfilter': myfilter, 'slink': slink}
    return render(request, 'volunteer/registration_view.html', context)


def profile_view(request, pk):
    cont = Contact.objects.all()  # Model Class Contact
    logo = Logo.objects.all()  # Model Class Logo
    slink = Social_link.objects.all()  # Model Class Social Link
    reg_view = get_object_or_404(Registration, pk=pk)
    context = {'cont': cont, 'logo': logo,
               'reg_view': reg_view, 'slink': slink}
    return render(request, 'volunteer/profile_view.html', context)


def form_view(request):
    cont = Contact.objects.all()  # Model Class Contact
    logo = Logo.objects.all()  # Model Class Logo
    slink = Social_link.objects.all()  # Model Class Social Link
    context = {'cont': cont, 'logo': logo, 'slink': slink}
    return render(request, 'volunteer/form_view.html', context)


def success_message(request):
    return render(request, 'volunteer/registration_success.html')
