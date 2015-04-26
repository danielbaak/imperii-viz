from django.shortcuts import render
from search.serializers import SearchSerializer
from search.models import Search
from django.http import Http404
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView


class SearchView(APIView):
    def get(self, request,format=None):
        events = Search.objects.all()
        serializer = SearchSerializer(events, many = True)
        return Response(serializer.data)

class SearchDetail(APIView):

    def get(self, request, pk, format=None):
        search = get_object_or_404(Search.objects.filter(pk=pk))
        serializer = SearchSerializer(search)
        return Response(serializer.data)
