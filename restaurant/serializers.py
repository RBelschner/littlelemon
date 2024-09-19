from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Menu, Booking

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu  # Use the Menu model
        fields = ['name', 'description', 'price', 'availability']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['name', 'description', 'price', 'availability']