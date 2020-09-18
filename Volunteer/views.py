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
    Volun_teen = Volunteer.objects.all()
    return render(request, 'volunteer/join_in_volunteer.html', {'cont': cont, 'logo': logo, 'Volun_teen': Volun_teen})

###############################################################################################


def registration(request):
    cont = Contact.objects.all()  # Model Class Contact
    logo = Logo.objects.all()  # Model Class Logo

    new_from = None
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            new_from = form.save(commit=False)
            new_from.save()
#--Email setting Start--#
            # cleaned_data from RegistrationForm
            Email_Name = form.cleaned_data['Email']
            # cleaned_data from RegistrationForm
            F_Name = form.cleaned_data['Full_Name']
            template = render_to_string(
                'volunteer/mail_temp.html', {'Name': F_Name})
            email = EmailMessage(
                'Thanks For Registration',
                template,
                settings.EMAIL_HOST_USER,
                [Email_Name],
            )
            email.fail_silently = False
            email.send()
#--Email setting End--#
            #messages.success(request, 'Form Submission Successful')
            return redirect('Message')

    else:
        form = RegistrationForm()

    return render(request, 'volunteer/registration_form.html', {'cont': cont, 'logo': logo, 'form': form, 'new_from': new_from})

###############################################################################################


def registration_view(request):
    cont = Contact.objects.all()  # Model Class Contact
    logo = Logo.objects.all()  # Model Class Logo
    reg_view = Registration.objects.all()
    myfilter = ProfileFilter(request.GET, queryset=reg_view)
    reg_view = myfilter.qs

    paginator = Paginator(reg_view, 10)
    page = request.GET.get('page')
    reg_view = paginator.get_page(page)

    context = {'cont': cont, 'logo': logo,
               'reg_view': reg_view, 'myfilter': myfilter}
    return render(request, 'volunteer/registration_view.html', context)


def profile_view(request, pk):
    cont = Contact.objects.all()  # Model Class Contact
    logo = Logo.objects.all()  # Model Class Logo
    reg_view = get_object_or_404(Registration, pk=pk)
    context = {'cont': cont, 'logo': logo, 'reg_view': reg_view}
    return render(request, 'volunteer/profile_view.html', context)


def form_view(request):
    cont = Contact.objects.all()  # Model Class Contact
    logo = Logo.objects.all()  # Model Class Logo
    context = {'cont': cont, 'logo': logo}
    return render(request, 'volunteer/form_view.html', context)


def success_message(request):
    return render(request, 'volunteer/success.html')
