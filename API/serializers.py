from .models import Car, User
from rest_framework import serializers


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields=['id', 'modl', 'brand', 'rentrate', 'buyrate', 'Customer', 'odometer', 'IsAvailable']


class UserSerializer(serializers.ModelSerializer):
    RentedCab = CarSerializer(many=True, read_only=False)
    RentedCab = serializers.StringRelatedField(many=True, read_only=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'mail', 'password', 'RentedCab']

