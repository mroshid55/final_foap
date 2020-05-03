from django.db import models


class Volunteer(models.Model):
    Title = models.CharField(max_length=200)
    Short_describe = models.CharField(max_length=250)
    Site_name = models.CharField(max_length=100)
    Link = models.CharField(max_length=500)
    Image = models.ImageField(upload_to='Volunteer')

###########################################################################
