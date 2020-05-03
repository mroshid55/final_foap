from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

# Register your models here.


class Chart_Admin(admin.ModelAdmin):
    list_display = ('Project', 'Value')
    list_filter = ('Project', 'Value')
    search_fields = ['Project', 'Value']


admin.site.register(Chart, Chart_Admin)

##################################################################################
