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
