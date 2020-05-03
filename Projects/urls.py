from django.urls import path
from . import views

urlpatterns = [

    path('on_going_projects',
         views.on_going_projects, name='on_going_projects'),

    path('completed_projects',
         views.completed_projects, name='completed_projects'),

    path('upcoming_projects',
         views.upcoming_projects, name='upcoming_projects')



]
