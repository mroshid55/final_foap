from django import forms
from crispy_forms.helper import FormHelper
from .models import *


class NewsletterSignUpForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_show_labels = False
    Email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'Input Your Email Address'}))

    class Meta:
        model = NewsletterUser
        fields = ['Email']

        def clean_email(self):
            Email = self.cleaned_date.get('Email')

            return Email
