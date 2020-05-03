from django.shortcuts import render, get_object_or_404
from .models import *
from Home_Page.models import *


#--volunteer page--#


def volunteer(request):
    cont = Contact.objects.all()  # Model Class Contact
    logo = Logo.objects.all()  # Model Class Logo
    Volun_teen = Volunteer.objects.all()
    return render(request, 'volunteer/join_in_volunteer.html', {'cont': cont, 'logo': logo, 'Volun_teen': Volun_teen})

###############################################################################################
