from django import forms


class GetForms(forms.Form):
    req = forms.CharField()
    loc = forms.CharField()
