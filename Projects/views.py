from django.shortcuts import render, get_object_or_404
from .models import *
from Home_Page.models import *
#--on going project page--#


def on_going_projects(request):
    cont = Contact.objects.all().order_by('-id')  # Model Class Contact
    logo = Logo.objects.all()  # Model Class Logo
    slink = Social_link.objects.all()  # Model Class Social Link
    ogp = On_going_projects.objects.all()
    return render(request, 'projects/on_going_projects.html', {'cont': cont, 'logo': logo, 'ogp': ogp, 'slink': slink})

###############################################################################################

#--completed project page--#


def completed_projects(request):
    cont = Contact.objects.all().order_by('-id')   # Model Class Contact
    logo = Logo.objects.all()  # Model Class Logo
    slink = Social_link.objects.all()  # Model Class Social Link
    ogp = Completed_projects.objects.all()
    return render(request, 'projects/completed_projects.html', {'cont': cont, 'logo': logo, 'ogp': ogp, 'slink': slink})

###############################################################################################

#--upcoming project page--#


def upcoming_projects(request):
    cont = Contact.objects.all().order_by('-id')   # Model Class Contact
    logo = Logo.objects.all()  # Model Class Logo
    slink = Social_link.objects.all()  # Model Class Social Link
    ogp = Upcoming_projects.objects.all()
    return render(request, 'projects/upcoming_projects.html', {'cont': cont, 'logo': logo, 'ogp': ogp, 'slink': slink})

###############################################################################################
