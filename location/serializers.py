__author__ = 'larissa'
from rest_framework import serializers
from location.models import Location


"""Serializer to return a Location with just the gps"""
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('latitude', 'longitude')