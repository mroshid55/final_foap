from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *


class About_Admin(admin.ModelAdmin):
    list_display = ('id', 'Details',
                    'Image')
    list_filter = ('id', 'Details', 'Image')
    search_fields = ['id', 'Image']


admin.site.register(About, About_Admin)
###########################################################################


class Why_choose_us_Admin(admin.ModelAdmin):
    list_display = ('id', 'Title')
    list_filter = ('id', 'Title')
    search_fields = ['id', 'Title']


admin.site.register(Why_choose_us, Why_choose_us_Admin)
############################################################################


class Activity_Admin(admin.ModelAdmin):
    list_display = ('Title', 'Value')
    list_filter = ('Title', 'Value')
    search_fields = ['Title', 'Value']


admin.site.register(Activity, Activity_Admin)

##################################################################################
