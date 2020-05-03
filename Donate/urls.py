from django.urls import path
from . import views

urlpatterns = [

    path('donate-info', views.donate, name='donate-info'),

    path('zakat-info', views.zakat, name='zakat-info'),


]
