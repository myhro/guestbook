from django import forms
from .models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        fields = ('name', 'avatar')
        model = Person
