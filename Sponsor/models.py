from django.db import models


# Class of Sponsor


class Sponsor(models.Model):
    Name = models.CharField(max_length=250, blank=True)
    Image = models.ImageField(upload_to='Sponsor')
