from django.shortcuts import render, get_object_or_404
from .models import *
from Home_Page.models import *


#--team page--#


def team(request):
    cont = Contact.objects.all()  # Model Class Contact
    logo = Logo.objects.all()  # Model Class Logo
    slink = Social_link.objects.all()  # Model Class Social Link
    team_mem = Team.objects.all().order_by('id')  # Model Class Team
    return render(request, 'team/meet_the_team.html', {'cont': cont, 'logo': logo, 'team_mem': team_mem, 'slink': slink})


def profile_view(request, pk):
    tm_id = get_object_or_404(Team, pk=pk)
    cont = Contact.objects.all()  # Model Class Contact
    logo = Logo.objects.all()  # Model Class Logo
    slink = Social_link.objects.all()  # Model Class Social Link
    return render(request, 'team/profile_view.html', {'tm_id': tm_id, 'cont': cont, 'logo': logo, 'slink': slink})


def doctor_team(request):
    cont = Contact.objects.all()  # Model Class Contact
    logo = Logo.objects.all()  # Model Class Logo
    slink = Social_link.objects.all()  # Model Class Social Link
    team_mem = Doctor_team.objects.all().order_by('id')  # Model Class Team
    return render(request, 'team/doctor_team.html', {'cont': cont, 'logo': logo, 'team_mem': team_mem, 'slink': slink})


def doctor_view(request, pk):
    tm_id = get_object_or_404(Doctor_team, pk=pk)
    cont = Contact.objects.all()  # Model Class Contact
    logo = Logo.objects.all()  # Model Class Logo
    slink = Social_link.objects.all()  # Model Class Social Link
    return render(request, 'team/doctor_view.html', {'tm_id': tm_id, 'cont': cont, 'logo': logo, 'slink': slink})


def adviser_team(request):
    cont = Contact.objects.all()  # Model Class Contact
    logo = Logo.objects.all()  # Model Class Logo
    slink = Social_link.objects.all()  # Model Class Social Link
    team_mem = Adviser_team.objects.all().order_by('id')  # Model Class Team
    return render(request, 'team/adviser_team.html', {'cont': cont, 'logo': logo, 'team_mem': team_mem, 'slink': slink})


def adviser_view(request, pk):
    tm_id = get_object_or_404(Adviser_team, pk=pk)
    cont = Contact.objects.all()  # Model Class Contact
    logo = Logo.objects.all()  # Model Class Logo
    slink = Social_link.objects.all()  # Model Class Social Link
    return render(request, 'team/adviser_view.html', {'tm_id': tm_id, 'cont': cont, 'logo': logo, 'slink': slink})


#--team profile view page--#

###############################################################################################
