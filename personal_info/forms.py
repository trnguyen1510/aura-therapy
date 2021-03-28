from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

from .models import Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        # Note that we didn't mention user field here.
        fields = ('middlename',
                    'date_of_birth',
                    'address',
                    'city',
                    'state',
                    'zip_code',
                    'phone',
                    'occupation',
                    'emergency_contact_first',
                    'emergency_contact_last',
                    'emergency_contact_phone',
                    'emergency_contact_email',
                    'emergency_contact_relationship',
                    'insurance',
                    'medication',
                    'reason_for_going_to_therapy',
                    'Do_you_smoke',
                    'alcohol',
                    'Seen_therapist',
                    'Married',
                    'Contact_method',
                    'medical_history',
                    'family_history',
                  )