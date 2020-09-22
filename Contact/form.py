from django import forms
from crispy_forms.helper import FormHelper
from .models import *


class ContactForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_show_labels = False
    Name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    Email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    Phone = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Phone'}))
    Body = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Message'}))

    class Meta:
        model = Message
        fields = ['Name', 'Email', 'Phone', 'Body', ]
