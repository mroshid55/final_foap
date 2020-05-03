from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField


# -- Class of Donate Model start--#


class Donate_Mobile(models.Model):
    Mobile_banking_name = models.CharField(max_length=80)
    Mobile_number = models.CharField(max_length=50)


class Donate_Bank(models.Model):
    Bank_name = models.CharField(max_length=40)
    Branch_name = models.CharField(max_length=35)
    Account_name = models.CharField(max_length=20)
    Account_number = models.CharField(max_length=30)
    Swift_code = models.CharField(max_length=20)

#-- Donate Model End --#

#-- Zakat Model Start --#


class Zakat_Mobile(models.Model):
    Mobile_banking_name = models.CharField(max_length=80)
    Mobile_number = models.CharField(max_length=50)


class Zakat_Bank(models.Model):
    Bank_name = models.CharField(max_length=40)
    Branch_name = models.CharField(max_length=35)
    Account_name = models.CharField(max_length=20)
    Account_number = models.CharField(max_length=30)
    Swift_code = models.CharField(max_length=20)


class Quran_hadith_info(models.Model):
    Quran_hadith = RichTextField()
    Source = models.CharField(max_length=50)

#-- Zakat Model End --#
###########################################################################
