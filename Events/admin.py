from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *
# Register your models here.


class Running_Event_Admin(admin.ModelAdmin):
    list_display = ('Title', 'Details', 'Location',
                    'Event_DT', 'Food', 'T_shirt', 'Active')
    list_filter = ('Title', 'Details', 'Location')
    search_fields = ['Title', 'Event_DT']


admin.site.register(Running_Event, Running_Event_Admin)


class Upcoming_event_Admin(admin.ModelAdmin):
    list_display = ('Title', 'Details', 'Location',
                    'Event_DT', 'Food', 'T_shirt', 'Active')
    list_filter = ('Title', 'Details', 'Location')
    search_fields = ['Title', 'Event_DT']


admin.site.register(Upcoming_Event, Upcoming_event_Admin)


class Completed_event_Admin(admin.ModelAdmin):
    list_display = ('Title', 'Details', 'Location',
                    'Event_DT', 'Active')
    list_filter = ('Title', 'Details', 'Location')
    search_fields = ['Title', 'Event_DT']


admin.site.register(Completed_Event, Completed_event_Admin)
##################################################################################
