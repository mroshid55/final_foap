from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *


class Sponsor_Admin(admin.ModelAdmin):
    list_display = ('id', 'Name', 'Image')
    list_filter = ('id', 'Name', 'Image')
    search_fields = ['id', 'Name']


admin.site.register(Sponsor, Sponsor_Admin)
