from django.shortcuts import render, get_object_or_404
from .models import *
from Home_Page.models import *


#--Running event page--#


def running_event(request):
    # Model class Call & pk Pass in url
    Re_list = Running_Event.objects.all().order_by('-id')
    cont = Contact.objects.all()  # Model Class Contact
    logo = Logo.objects.all()  # Model Class Logo
    return render(request, 'event_news/running_event.html', {'Re_list': Re_list, 'cont': cont, 'logo': logo})

#--Running event view page--#


def running_event_view(request, pk):
    rv = get_object_or_404(Running_Event, pk=pk)
    cont = Contact.objects.all()  # Model Class Contact
    logo = Logo.objects.all()  # Model Class Logo
    return render(request, 'event_news/running_detail.html', {'rv': rv, 'cont': cont, 'logo': logo})

#--upcoming event page--#


def upcoming_event(request):
    # Model class Call & pk Pass in url
    Up_list = Upcoming_Event.objects.all().order_by('-id')
    cont = Contact.objects.all()  # Model Class Contact
    logo = Logo.objects.all()  # Model Class Logo
    return render(request, 'event_news/upcoming_event.html', {'Up_list': Up_list, 'cont': cont, 'logo': logo})

#--upcoming event view page--#


def upcoming_event_view(request, pk):
    uev = get_object_or_404(Upcoming_Event, pk=pk)
    cont = Contact.objects.all()  # Model Class Contact
    logo = Logo.objects.all()  # Model Class Logo
    return render(request, 'event_news/upcoming_detail.html', {'uev': uev, 'cont': cont, 'logo': logo})


def completed_event(request):
    # Model class Call & pk Pass in url
    Up_list = Completed_Event.objects.all().order_by('-id')
    cont = Contact.objects.all()  # Model Class Contact
    logo = Logo.objects.all()  # Model Class Logo
    return render(request, 'event_news/completed_event.html', {'Up_list': Up_list, 'cont': cont, 'logo': logo})

#--upcoming event view page--#


def completed_event_view(request, pk):
    uev = get_object_or_404(Completed_Event, pk=pk)
    cont = Contact.objects.all()  # Model Class Contact
    logo = Logo.objects.all()  # Model Class Logo
    return render(request, 'event_news/completed_detail.html', {'uev': uev, 'cont': cont, 'logo': logo})

###############################################################################################
