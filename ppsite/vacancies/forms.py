from django import forms
from .models import Vacancies

class SearchForm(forms.Form):
    query = forms.CharField()   

class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancies
        fields = ['name', 'slug', 'body', 'status']
