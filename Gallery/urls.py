from django.urls import path
from . import views

urlpatterns = [

    path('video_gallery', views.video, name='video_gallery'),

    path('image_gallery', views.image, name='image_gallery')


]
