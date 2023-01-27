from django import forms
from .models import Choice


class GetForms(forms.Form):
    locations = forms.CharField(max_length=100)
    keyword = forms.CharField(max_length=100)


