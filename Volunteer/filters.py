from .models import *
import django_filters


class ProfileFilter(django_filters.FilterSet):
    class Meta:
        model = Registration
        fields = ('id', 'Full_Name', 'Contact')
