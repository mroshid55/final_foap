from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField


class About(models.Model):
    Details = RichTextField()
    Image = models.ImageField(upload_to='About')


class Why_choose_us(models.Model):
    Title = models.CharField(max_length=350)


class Activity(models.Model):
    Title = models.CharField(max_length=350)
    Value = models.IntegerField(default=0)
