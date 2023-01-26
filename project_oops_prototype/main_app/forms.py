from django import forms
from dataclasses import field
from .models import Station_search


class SearchForm(forms.ModelForm):
    class Meta:
        model = Station_search
        # fields = '__all__'
        fields = ['words']