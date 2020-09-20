from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *
# Register your models here.

admin.site.site_header = 'Foap Dashboard'
admin.site.site_title = 'Foap'
admin.site.index_title = 'Foap Administration'


class Contact_Admin(admin.ModelAdmin):
    list_display = ('Organization_name', 'Address',
                    'Phone', 'Mail', 'Meet_Time')
    list_filter = ('Organization_name', 'Address', 'Phone', 'Mail')
    search_fields = ['Address', 'Phone']


admin.site.register(Contact, Contact_Admin)

##################################################################################


class Logo_Admin(admin.ModelAdmin):
    list_display = ('id', 'Primary_logo', 'Secondary_logo')
    list_filter = ('id', 'Primary_logo', 'Secondary_logo')


admin.site.register(Logo, Logo_Admin)

##################################################################################


class Slider_Admin(admin.ModelAdmin):
    list_display = ('Slider_title', 'Location', 'Slider_img')
    list_filter = ('Slider_title', 'Location', 'Slider_img')
    search_fields = ['Slider_title', 'Location']


admin.site.register(Slider, Slider_Admin)
##################################################################################


class Foap_Admin(admin.ModelAdmin):
    list_display = ('First_letter', 'Full_name', 'Details')
    list_filter = ('First_letter', 'Full_name')
    search_fields = ['Title', 'Event_DT']


admin.site.register(FOAP, Foap_Admin)
##################################################################################


class Package_Admin(admin.ModelAdmin):
    list_display = ('Title', 'Amount', 'Choice', 'Link', 'Button_name')
    list_filter = ('Title', 'Amount', 'Choice')
    search_fields = ['Title', 'Amount']


admin.site.register(Package, Package_Admin)

##################################################################################


class News_Admin(admin.ModelAdmin):
    list_display = ('Title', 'Short_describe', 'Details')
    list_filter = ('Title', 'Image_post', 'Date_time')
    search_fields = ['Title', 'Date_time']


admin.site.register(New, News_Admin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Comment, CommentAdmin)


##################################################################################
class Event_Admin(admin.ModelAdmin):
    list_display = ('Title', 'Event_DT', 'Events_Image')
    list_filter = ('Title', 'Event_DT', 'Events_Image')
    search_fields = ['Title', 'Event_DT']


admin.site.register(Event, Event_Admin)

##################################################################################


class Review_Admin(admin.ModelAdmin):
    list_display = ('Name', 'Designation', 'Comment')
    list_filter = ('Name', 'Designation', 'Image_review')
    search_fields = ['Name', 'Designation']


admin.site.register(Review, Review_Admin)
##################################################################################


class Social_link_Admin(admin.ModelAdmin):
    list_display = ('Name', 'Href', 'Class_Name')
    list_filter = ('Name', 'Class_Name')
    search_fields = ['Name', 'Class_Name']


admin.site.register(Social_link, Social_link_Admin)
##################################################################################
