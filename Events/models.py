from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
#--EVENT MODEL--#


class Running_Event(models.Model):
    Select_value1 = (('No', 'No'),
                     ('Breakfast', 'Breakfast'),
                     ('Lunch', 'Lunch'),
                     ('Dinner', 'Dinner'),
                     ('Snacks', 'Snacks'))
    Select_value2 = (('Yes', 'Yes'),
                     ('No', 'No'))
    Title = models.CharField(max_length=150)
    Guest = models.CharField(max_length=100, blank=True)
    Contact = models.CharField(max_length=100, blank=True)
    Details = RichTextField(blank=True)
    Location = models.CharField(max_length=250)
    Event_DT = models.DateTimeField('Date_Publish')
    Food = models.CharField(max_length=15, choices=Select_value1)
    T_shirt = models.CharField(max_length=5, choices=Select_value2)
    Active = models.BooleanField(default=False)


class Upcoming_Event(models.Model):
    Select_value1 = (('No', 'No'),
                     ('Breakfast', 'Breakfast'),
                     ('Lunch', 'Lunch'),
                     ('Dinner', 'Dinner'),
                     ('Snacks', 'Snacks'))
    Select_value2 = (('Yes', 'Yes'),
                     ('No', 'No'))
    Title = models.CharField(max_length=150)
    Guest = models.CharField(max_length=100, blank=True)
    Contact = models.CharField(max_length=100, blank=True)
    Details = RichTextField(blank=True)
    Location = models.CharField(max_length=250)
    Event_DT = models.DateTimeField('Date_Publish')
    Food = models.CharField(max_length=15, choices=Select_value1)
    T_shirt = models.CharField(max_length=5, choices=Select_value2)
    Active = models.BooleanField(default=False)


class Completed_Event(models.Model):
    Title = models.CharField(max_length=150)
    Guest = models.CharField(max_length=100, blank=True)
    Details = RichTextField(blank=True)
    Location = models.CharField(max_length=250)
    Event_DT = models.DateTimeField('Date_Publish')
    Active = models.BooleanField(default=False)
###########################################################################
