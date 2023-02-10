from django.contrib import admin
from .models import Car
# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    readonly_fields = ('id','vin')
