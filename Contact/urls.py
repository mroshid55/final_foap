from django.urls import path
from . import views

urlpatterns = [

    path('contact_info', views.contact_info, name='contact_info')

]
