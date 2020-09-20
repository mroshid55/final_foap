from django.db import models

# Create your models here.


class NewsletterUser(models.Model):
    Email = models.EmailField(max_length=254)
    Date_Added = models.DateTimeField(auto_now_add=True)
