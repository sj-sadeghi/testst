from django import forms

from .models import Person
from .models import Mark


class Marks(forms.ModelForm):
    person = forms.ModelChoiceField(Person.objects.all(), label='Name')
    grade = forms.CharField(label='Mark')

    class Meta:
        model = Mark
        fields = ['person', 'grade']
