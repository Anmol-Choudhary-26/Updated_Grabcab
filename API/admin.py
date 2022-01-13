import imp
from django.contrib import admin
from .models import Car, User
# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display=['id', 'modl', 'brand', 'rentrate', 'buyrate', 'Customer', 'odometer', 'IsAvailable']
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['id', 'username', 'mail', 'password']
  
