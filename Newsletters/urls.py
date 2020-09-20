from django.urls import path
from . import views

urlpatterns = [


    path('newslettersignup', views.newslettersignup,
         name='newslettersignup'),

    path('Message', views.success_message, name='Message')



]
