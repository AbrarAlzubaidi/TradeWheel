from django import forms

from .models import Car

class AddCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = (
            'title',
            'description',
            'brand',
            'model',
            'vin',
            'mileage',
            'engine',
            'transmission',
            'color',
            'image' 
            )

    # def save(self, commit=False):
    #     pass