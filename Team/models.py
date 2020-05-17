from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField


class Team(models.Model):
    active_value = (('I AM NEW!', 'I AM NEW!'),
                    ('I AM OLD!', 'I AM OLD!'))
    Name = models.CharField(max_length=100)
    Designation = models.CharField(max_length=100)
    Phone = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Bio_data = RichTextField(blank=True)
    Image = models.ImageField(upload_to='Team')
    status = models.CharField(
        max_length=12, choices=active_value)


class Doctor_team(models.Model):
    Name = models.CharField(max_length=100)
    Designation = models.CharField(max_length=100)
    Registration = models.CharField(max_length=100, blank=True)
    Working_Area = models.CharField(max_length=100)
    Phone = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Image = models.ImageField(upload_to='Doctor_team')


class Adviser_team(models.Model):
    Name = models.CharField(max_length=100)
    Designation = models.CharField(max_length=100)
    Phone = models.CharField(max_length=50)
    Email = models.CharField(max_length=50, blank=True)
    Image = models.ImageField(upload_to='Adviser_team')
