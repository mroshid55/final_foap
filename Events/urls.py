from django.urls import path
from . import views

urlpatterns = [

    path('running_event', views.running_event,
         name='running_event'),

    path('running_detail/<str:pk>',
         views.running_event_view, name='running_detail'),

    path('upcoming_event', views.upcoming_event,
         name='upcoming_event'),

    path('upcoming_detail/<str:pk>',
         views.upcoming_event_view, name='upcoming_detail'),

    path('completed_event', views.completed_event,
         name='completed_event'),

    path('completed_detail/<str:pk>',
         views.completed_event_view, name='completed_detail')


]
