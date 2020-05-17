from django.urls import path
from . import views

urlpatterns = [

    path('about-info', views.about, name='about-info'),

    path('mission_statement', views.mission, name='mission_statement'),

    path('vision_statement', views.vision, name='vision_statement')


]
