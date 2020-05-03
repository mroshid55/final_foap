from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *


class Team_Admin(admin.ModelAdmin):
    list_display = ('Name', 'Designation', 'Phone', 'Email', 'status', 'Image')
    list_filter = ('Name', 'Designation', 'Phone')
    search_fields = ['Name', 'Designation', 'Phone']


admin.site.register(Team, Team_Admin)


class Doctor_Team_Admin(admin.ModelAdmin):
    list_display = ('Name', 'Designation', 'Registration',
                    'Working_Area', 'Phone', 'Email')
    list_filter = ('Name', 'Designation', 'Phone')
    search_fields = ['Name', 'Designation', 'Phone']


admin.site.register(Doctor_team, Doctor_Team_Admin)

##################################################################################
