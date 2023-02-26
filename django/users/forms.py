from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Location, Profile
from .widgets import CustomImageField

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

class ProfileUserForm(forms.ModelForm):
    username = forms.CharField(disabled=True)
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email'
        )

class ProfileForm(forms.ModelForm):
    photo = forms.ImageField(widget=CustomImageField)
    bio = forms.TextInput()
    
    class Meta:
        model = Profile
        fields = (
            'phone_number',
            'bio',
            'photo',
        )
