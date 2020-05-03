from django.shortcuts import render, get_object_or_404
from .models import *
from Home_Page.models import *


#--donate page--#


def donate(request):
    cont = Contact.objects.all()  # Model Class Contact
    logo = Logo.objects.all()  # Model Class Logo
    d_m = Donate_Mobile.objects.all()  # Model Class Mobile_banking_info
    d_b = Donate_Bank.objects.all()  # Model Class Bank_account_info

    context = {'cont': cont, 'logo': logo,
               'd_m': d_m, 'd_b': d_b}
    return render(request, 'donate/donate_info.html', context)

#--zakat page--#


def zakat(request):
    cont = Contact.objects.all()  # Model Class Contact
    logo = Logo.objects.all()  # Model Class Logo
    z_m = Zakat_Mobile.objects.all()  # Model Class Mobile_banking_info
    z_b = Zakat_Bank.objects.all()  # Model Class Bank_account_info
    hadith = Quran_hadith_info.objects.all()  # Model Class Quran_hadith_info

    context = {'cont': cont, 'logo': logo,
               'z_m': z_m, 'z_b': z_b, 'hadith': hadith}
    return render(request, 'donate/zakat_info.html', context)

###############################################################################################
