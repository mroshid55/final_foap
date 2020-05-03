from django.db import models

# Create your models here.


class Chart(models.Model):
    Project = models.CharField(max_length=250)
    Value = models.IntegerField()

###########################################################################
