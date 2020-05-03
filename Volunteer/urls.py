from django.urls import path
from . import views

urlpatterns = [


    path('join_in_volunteer', views.volunteer,
         name='join_in_volunteer')

]
