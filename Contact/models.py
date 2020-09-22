from django.db import models

# Create your models here.


class Message(models.Model):
    Name = models.CharField(max_length=150)
    Email = models.EmailField(max_length=254)
    Phone = models.CharField(max_length=150)
    Body = models.CharField(max_length=350)
    Date_Added = models.DateTimeField(auto_now_add=True)
