from django.shortcuts import render
from person.serializers import PersonSerializer
from person.models import Person
from django.http import Http404
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView


class PersonView(APIView):
    def get(self, request,format=None):
        events = Person.objects.all()
        serializer = PersonSerializer(events, many = True)
        return Response(serializer.data)

class PersonDetail(APIView):

    def get(self, request, pk, format=None):
        person = get_object_or_404(Person.objects.filter(pk=pk))
        serializer = PersonSerializer(person)
        return Response(serializer.data)
