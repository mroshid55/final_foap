from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField


#-- Project Model start --#


class On_going_projects(models.Model):
    Title = models.CharField(max_length=150)
    Pdf_file = models.FileField(upload_to='On_going_project/%Y/%m/%d/')


class Completed_projects(models.Model):
    Title = models.CharField(max_length=150)
    Pdf_file = models.FileField(upload_to='Completed_project/%Y/%m/%d/')


class Upcoming_projects(models.Model):
    Title = models.CharField(max_length=150)
    Pdf_file = models.FileField(upload_to='Upcoming_projects/%Y/%m/%d/')

#-- Project Model End --#
###########################################################################
