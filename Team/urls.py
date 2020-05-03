from django.urls import path
from . import views

urlpatterns = [


    path('meet_the_team', views.team, name='meet_the_team'),

    path('Profile_view/<str:pk>',
         views.profile_view, name='Profile_view'),

    path('doctor_team', views.doctor_team, name='doctor_team'),

    path('doctor_view/<str:pk>',
         views.doctor_view, name='doctor_view'),



]
