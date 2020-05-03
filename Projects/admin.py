from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *



class On_going_projects_Admin(admin.ModelAdmin):
    list_display = ('Title', 'Pdf_file')
    list_filter = ('Title', 'Pdf_file')
    search_fields = ['Title']


admin.site.register(On_going_projects, On_going_projects_Admin)

##################################################################################


class Completed_projects_Admin(admin.ModelAdmin):
    list_display = ('Title', 'Pdf_file')
    list_filter = ('Title', 'Pdf_file')
    search_fields = ['Title']


admin.site.register(Completed_projects, Completed_projects_Admin)

##################################################################################


class Upcoming_projects_Admin(admin.ModelAdmin):
    list_display = ('Title', 'Pdf_file')
    list_filter = ('Title', 'Pdf_file')
    search_fields = ['Title']


admin.site.register(Upcoming_projects, Upcoming_projects_Admin)

##################################################################################
