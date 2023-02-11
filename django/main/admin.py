from django.contrib import admin
from .models import Car, UsersLikedCars

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    readonly_fields = ('id','vin')


@admin.register(UsersLikedCars)
class UsersLikedCarsAdmin(admin.ModelAdmin):
    pass