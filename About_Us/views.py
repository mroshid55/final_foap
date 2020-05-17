from django.shortcuts import render, get_object_or_404
from .models import *
from Home_Page.models import *


#--about page--#


def about(request):
    cont = Contact.objects.all()  # Model Class Contact
    logo = Logo.objects.all()  # Model Class Logo
    ab = About.objects.all()
    cu = Why_choose_us.objects.all().order_by('id')
    av = Activity.objects.all().order_by('id')
    context = {'ab': ab, 'cont': cont, 'logo': logo, 'cu': cu, 'av': av}
    return render(request, 'about_us/about_info.html', context)

###############################################################################################


def mission(request):
    cont = Contact.objects.all()  # Model Class Contact
    logo = Logo.objects.all()  # Model Class Logo
    mn = Mission.objects.all()
    context = {'cont': cont, 'logo': logo, 'mn': mn}
    return render(request, 'about_us/mission_statement.html', context)


def vision(request):
    cont = Contact.objects.all()  # Model Class Contact
    logo = Logo.objects.all()  # Model Class Logo
    vn = Vission.objects.all()
    context = {'cont': cont, 'logo': logo, 'vn': vn}
    return render(request, 'about_us/vision_statement.html', context)
