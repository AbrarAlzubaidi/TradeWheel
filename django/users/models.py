from django.db import models
from django.contrib.auth.models import User
from localflavor.us.models import USStateField, USZipCodeField

class Location(models.Model):
    address_1 = models.CharField(max_length=128, blank=True)
    address_2 = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=64)
    state = USStateField(default='NY')
    zip_code = USZipCodeField(null=True)

    def __str__(self):
        return f'location {self.id}'


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12, blank=True)
    photo = models.ImageField(null=True)
    bio = models.CharField(max_length=100, blank=True)
    location = models.OneToOneField(Location, on_delete=models.CASCADE, related_name='location', null=True)

    def __str__(self):
        return f'{self.user.username}\'s profile'



