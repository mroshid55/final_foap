from django.db import models


class Volunteer(models.Model):
    Title = models.CharField(max_length=200)
    Short_describe = models.CharField(max_length=250)
    Site_name = models.CharField(max_length=100)
    Link = models.CharField(max_length=500)
    Image = models.ImageField(upload_to='Volunteer')

###########################################################################


class Registration(models.Model):
    Select_value1 = (('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'))
    Select_value2 = (('Male', 'Male'), ('Female', 'Female'),
                     ('Others', 'Others'))
    Select_value3 = (('Do not know yet', 'Do not know yet'),
                     ('A+', 'A+'), ('B+', 'B+'), ('AB+', 'AB+'), ('O+', 'O+'),
                     ('A-', 'A-'), ('B-', 'B-'), ('AB-', 'AB-'), ('O-', 'O-'))
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Full_Name = models.CharField(max_length=150)
    Father_Name = models.CharField(max_length=50)
    Mother_Name = models.CharField(max_length=50)
    Institute = models.CharField(max_length=150)
    Contact = models.CharField(max_length=50)
    Address = models.TextField()
    Date_of_Birth = models.DateField()
    Email = models.EmailField()
    T_Shairt = models.CharField(max_length=6, choices=Select_value1)
    Gender = models.CharField(max_length=15, choices=Select_value2)
    Blood_Group = models.CharField(max_length=20, choices=Select_value3)
    I_Agree_to_Terms = models.BooleanField(default=False)
