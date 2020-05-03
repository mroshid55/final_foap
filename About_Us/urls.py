from django.urls import path
from . import views

urlpatterns = [

    path('about-info', views.about, name='about-info')


]
