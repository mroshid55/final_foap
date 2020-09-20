from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *


# Register your models here.


class NewsletterUser_Admin(admin.ModelAdmin):
    list_display = ('Email', 'Date_Added')
    list_filter = ('Email', 'Date_Added')
    search_fields = ['Email', 'Date_Added']


admin.site.register(NewsletterUser, NewsletterUser_Admin)
##################################################################################
