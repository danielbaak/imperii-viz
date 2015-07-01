__author__ = 'larissa'

from rest_framework import serializers
from person.models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'name', 'short_description', 'birth_date','death_date','gnd_number', 'img_url')
