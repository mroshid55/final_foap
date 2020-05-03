from django.db import models
from datetime import datetime
from embed_video.fields import EmbedVideoField
from ckeditor.fields import RichTextField

# Class of Gallery


class Image_Gallery(models.Model):
    Event_DT = models.CharField(max_length=150, blank=True)
    Short_describe = models.CharField(max_length=250, blank=True)
    Details = RichTextField()
    Gallery_image = models.ImageField(upload_to='Gallery')
    Active = models.BooleanField(default=False)


###########################################################################
class Video_Gallery(models.Model):
    Title = models.CharField(max_length=150)
    Short_describe = models.CharField(max_length=350, blank=True)
    video = EmbedVideoField(blank=True)
    Date = models.DateTimeField('Date_Publish')
###########################################################################
