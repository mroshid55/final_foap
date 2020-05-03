from django.urls import path
from . import views

urlpatterns = [

    path('program_chart', views.chart, name='program_chart')


]
