import uuid
from datetime import datetime   
from django.db import models
from users.models import Profile, Location
from .constants import CAR_BRANDS, TRANSMISSIONS_OPTIONS
from .utils import upload_image

# Create your models here.
class Car(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4)
    title = models.CharField(max_length=100, null=False, default=None)
    description = models.TextField(null=True)
    brand = models.CharField(max_length=24, default=None,choices=CAR_BRANDS)
    model = models.CharField(max_length=64, default=None)
    vin = models.CharField(max_length=17, default=None)
    mileage = models.IntegerField(default=0)
    engine = models.CharField(max_length=24, default=None)
    transmission = models.CharField(max_length=24, choices=TRANSMISSIONS_OPTIONS, default=None)
    color = models.CharField(max_length=24, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    location = models.OneToOneField(Location, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to=upload_image, null=True, blank=True)
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.seller.user.username} {self.model} car'
    

class UsersLikedCars(models.Model):
    # it a M:N relation ship between the profile and the cars 
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    liked_date = models.DateTimeField(auto_now_add=True, blank=True, null=True) 

    def __str__(self):
        return f'user {self.profile.user.username} liked car {self.car.model}'