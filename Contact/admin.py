from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *


# Register your models here.


class Message_Admin(admin.ModelAdmin):
    list_display = ('Name', 'Email', 'Phone', 'Body', 'Date_Added')
    list_filter = ('Name', 'Email', 'Phone')
    search_fields = ['Name', 'Email', 'Phone']


admin.site.register(Message, Message_Admin)
##################################################################################
