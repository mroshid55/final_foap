from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

# Register your models here.


class Gallery_Admin(admin.ModelAdmin):
    list_display = ('Event_DT', 'Short_describe',
                    'Details', 'Gallery_image', 'Active')
    list_filter = ('id', 'Event_DT', 'Gallery_image')
    search_fields = ['id', 'Event_DT', 'Gallery_image']


admin.site.register(Image_Gallery, Gallery_Admin)

##################################################################################


class Video_Admin(admin.ModelAdmin):
    list_display = ('Title', 'Short_describe', 'video', 'Date')
    list_filter = ('id', 'Title', 'Short_describe', 'Date')
    search_fields = ['id', 'Date']


admin.site.register(Video_Gallery, Video_Admin)
