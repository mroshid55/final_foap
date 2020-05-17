from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *


class Volunteer_Admin(admin.ModelAdmin):
    list_display = ('Title', 'Short_describe',
                    'Site_name', 'Link')
    list_filter = ('Site_name', 'Image')
    search_fields = ['Site_name']


admin.site.register(Volunteer, Volunteer_Admin)
##################################################################################


class Registration_Admin(admin.ModelAdmin):
    list_display = ('Full_Name', 'Father_Name', 'Mother_Name', 'Address', 'Institute',
                    'Contact', 'Email', 'T_Shairt', 'Gender', 'Blood_Group', 'Date_of_Birth')
    list_filter = ('Full_Name', 'Full_Name', 'Date_of_Birth', 'Contact')
    search_fields = ['Full_Name', 'Contact', 'Date_of_Birth']


admin.site.register(Registration, Registration_Admin)
##################################################################################
