from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Location

from localflavor.us.forms import USZipCodeField

class NewUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        if commit:
            user.save()
        return user


class LocationForm(forms.ModelForm):
    address_1 = forms.CharField(max_length=128, required=True)
    
    class Meta:
        model= Location
        fields = (
            'address_1',
            'address_2',
            'city',
            'state',
            'zip_code'
        )