__author__ = 'daniel'

from rest_framework import serializers
from search.models import Search

class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Search
        fields = ('name', 'short_description', 'birth_date','death_date','gnd_number')
