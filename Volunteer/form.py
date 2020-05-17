from .models import *
from django import forms


class RegistrationForm(forms.ModelForm):
    First_Name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your First Name'}))
    Last_Name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your Last Name'}))
    Full_Name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your Full Name'}))
    Father_Name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your Father Name'}))
    Mother_Name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your Mother Name'}))
    Institute = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your Institute Name'}))
    Contact = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your Contact Number'}))
    Address = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your Address'}))
    Email = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your Email Address'}))
    Date_of_Birth = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}))
    I_Agree_to_Terms = forms.BooleanField(
        error_messages={
            'required': 'You must accept the terms and conditions'},
        label="Terms&Conditions"
    )

    class Meta:
        model = Registration
        fields = ('First_Name', 'Last_Name', 'Full_Name', 'Father_Name', 'Mother_Name', 'Institute', 'Contact',
                  'Address', 'Email', 'Date_of_Birth', 'T_Shairt', 'Gender', 'Blood_Group', 'I_Agree_to_Terms')
