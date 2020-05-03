from django.shortcuts import render, get_object_or_404
from .models import *
from Home_Page.models import *


#--sponsor page--#


def sponsor(request):
    cont = Contact.objects.all()  # Model Class Contact
    logo = Logo.objects.all()  # Model Class Logo
    sp = Sponsor.objects.all().order_by('-id')
    return render(request, 'sponsor/our_sponsor.html', {'cont': cont, 'logo': logo, 'sp': sp})
