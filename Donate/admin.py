from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *


class Donate_Mobile_Admin(admin.ModelAdmin):
    list_display = ('Mobile_banking_name', 'Mobile_number')
    list_filter = ('Mobile_banking_name', 'Mobile_number')
    search_fields = ['Mobile_banking_name', 'Mobile_number']


admin.site.register(Donate_Mobile, Donate_Mobile_Admin)

##################################################################################


class Donate_Bank_Admin(admin.ModelAdmin):
    list_display = ('Bank_name', 'Branch_name',
                    'Account_name', 'Account_number', 'Swift_code')
    list_filter = ('Bank_name', 'Account_name', 'Branch_name')
    search_fields = ['Bank_name', 'Account_name']


admin.site.register(Donate_Bank, Donate_Bank_Admin)

##################################################################################


class Zakat_Mobile_Admin(admin.ModelAdmin):
    list_display = ('Mobile_banking_name', 'Mobile_number')
    list_filter = ('Mobile_banking_name', 'Mobile_number')
    search_fields = ['Mobile_banking_name', 'Mobile_number']


admin.site.register(Zakat_Mobile, Zakat_Mobile_Admin)

##################################################################################


class Zakat_Bank_Admin(admin.ModelAdmin):
    list_display = ('Bank_name', 'Branch_name',
                    'Account_name', 'Account_number', 'Swift_code')
    list_filter = ('Bank_name', 'Account_name', 'Branch_name')
    search_fields = ['Bank_name', 'Account_name']


admin.site.register(Zakat_Bank, Zakat_Bank_Admin)


class Quran_hadith_info_Admin(admin.ModelAdmin):
    list_display = ('id', 'Quran_hadith', 'Source')
    list_filter = ('id', 'Source')
    search_fields = ['id', 'Source']


admin.site.register(Quran_hadith_info, Quran_hadith_info_Admin)
