__author__ = 'larissa'

from rest_framework import serializers
from regeste.models import Regeste
from location.serializers import LocationSerializer

class RegesteSerializer(serializers.ModelSerializer):
    #StringRelatedField may be used to represent the target of the relationship using its __unicode__ method.
    #many - If applied to a to-many relationship, you should set this argument to True.
    #only one issuer
    issuer = serializers.StringRelatedField()


    #http://www.django-rest-framework.org/api-guide/relations/#nested-relationships
    place_of_issue = LocationSerializer(many=False)

    class Meta:
        model = Regeste
        fields = ('title', 'place_of_issue', 'issuer', 'issue_date', 'abstract', 'analysis', 'addenda', 'locations')

