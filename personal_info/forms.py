from django import forms
from .models import Person
from django.forms import ModelForm


class personform(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        widgets = {'Do_you_smoke': forms.RadioSelect, 'alcohol': forms.RadioSelect, 'Seen_therapist': forms.RadioSelect,  'Married': forms.RadioSelect, 'Contact_method': forms.RadioSelect, \
        'medical_history': forms.RadioSelect, 'family_history': forms.RadioSelect
         } 