from django.urls import path
from . import views

urlpatterns = [


    path('join_in_volunteer', views.volunteer,
         name='join_in_volunteer'),

    path('form_view', views.form_view,
         name='form_view'),

    path('registration_form', views.registration,
         name='registration_form'),

    path('registration_view', views.registration_view,
         name='registration_view'),

    path('profile_view/<str:pk>', views.profile_view,
         name='profile_view'),

    path('Registration_Message', views.success_message,
         name='Registration_Message')



]
