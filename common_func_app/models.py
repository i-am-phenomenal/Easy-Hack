from django.db import models
from django import forms
# Create your models here.


class SearchText(forms.Form):
    searchText = forms.CharField(
        label="searchText", max_length=100, required=True)