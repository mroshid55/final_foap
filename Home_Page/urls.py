from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('index/', views.master, name='master'),

    path('blog/blog_detail/<str:pk>',
         views.blog_detail, name='blog/blog_detail'),

]
