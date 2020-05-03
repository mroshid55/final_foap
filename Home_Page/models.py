from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField


class Contact(models.Model):
    Organization_name = models.CharField(max_length=100)
    Address = models.CharField(max_length=150)
    Phone = models.CharField(max_length=100)
    Mail = models.CharField(max_length=100)
    Meet_Time = models.CharField(max_length=50)

#########################################################################
# Class of Logo


class Logo(models.Model):
    Primary_logo = models.ImageField(upload_to='Logo')
    Secondary_logo = models.ImageField(upload_to='Logo')

###########################################################################
# Class of Slider


class Slider(models.Model):
    Slider_title = models.CharField(max_length=250)
    Location = models.CharField(max_length=150)
    Slider_img = models.ImageField(upload_to='Slider')
###########################################################################


class FOAP(models.Model):
    First_letter = models.CharField(max_length=1)
    Full_name = models.CharField(max_length=50)
    Details = RichTextField(blank=True)
###########################################################################


class Package(models.Model):
    Select_value = (('Day', 'Day'),
                    ('Month', 'Month'),
                    ('Year', 'Year'))
    Title = models.CharField(max_length=150)
    Field_1 = models.CharField(max_length=250, blank=True)
    Field_2 = models.CharField(max_length=250, blank=True)
    Field_3 = models.CharField(max_length=250, blank=True)
    Field_4 = models.CharField(max_length=250, blank=True)
    Field_5 = models.CharField(max_length=250, blank=True)
    Amount = models.IntegerField()
    Choice = models.CharField(max_length=10, choices=Select_value)
    Link = models.CharField(max_length=150)
    Button_name = models.CharField(max_length=50)

###########################################################################
# Class of News Post


class New(models.Model):
    Title = models.CharField(max_length=100)
    Short_describe = models.CharField(max_length=150)
    Details = RichTextField()
    Date_time = models.DateTimeField(auto_now_add=True)
    Image_post = models.ImageField(upload_to='News')
# blog post comment model


class Comment(models.Model):
    post = models.ForeignKey(
        New, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

###########################################################################
# Class of Events


class Event(models.Model):
    Title = models.CharField(max_length=150)
    Event_DT = models.DateTimeField('Date_Publish')
    Events_Image = models.ImageField(upload_to='Event')

###########################################################################
# Class of Review


class Review(models.Model):
    Name = models.CharField(max_length=50)
    Designation = models.CharField(max_length=100)
    Comment = RichTextField()
    Image_review = models.ImageField(upload_to='Review')

###########################################################################
