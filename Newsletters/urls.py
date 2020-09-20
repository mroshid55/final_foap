from django.urls import path
from . import views

urlpatterns = [


    path('newslettersignup', views.newslettersignup,
         name='newslettersignup'),

    path('SignUp_Message', views.success_message_newsletters, name='SignUp_Message')



]
