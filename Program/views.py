from django.shortcuts import render, get_object_or_404
from .models import *
from Home_Page.models import *

#--program chart page--#


def chart(request):
    cont = Contact.objects.all()  # Model Class Contact
    logo = Logo.objects.all()  # Model Class Logo
    context = Chart.objects.all()
    return render(request, 'charts/program_chart.html', {'cont': cont, 'logo': logo, 'context': context})

###############################################################################################
