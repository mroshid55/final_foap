from django.shortcuts import render, get_object_or_404
from .models import *
from Home_Page.models import *


#--video gallery page--#


def video(request):
    vg = Video_Gallery.objects.all().order_by('-id')
    cont = Contact.objects.all()  # Model Class Contact
    logo = Logo.objects.all()  # Model Class Logo
    return render(request, 'gallery/video.html', {'vg': vg, 'cont': cont, 'logo': logo})

###############################################################################################

#--image gallery page--#


def image(request):
    g_image = Image_Gallery.objects.all().order_by('-id')
    cont = Contact.objects.all()  # Model Class Contact
    logo = Logo.objects.all()  # Model Class Logo
    return render(request, 'gallery/image.html', {'g_image': g_image, 'cont': cont, 'logo': logo})

###############################################################################################
