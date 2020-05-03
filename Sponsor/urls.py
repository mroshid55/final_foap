from django.urls import path
from . import views

urlpatterns = [

    path('our_sponsor', views.sponsor, name='our_sponsor')

]
