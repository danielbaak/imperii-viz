from regeste.serializers import RegesteSerializer
from person.models import Person
from regeste.models import Regeste
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView


class RegestDetail(APIView):

    def get(self, request, pk, format=None):
        regeste = get_object_or_404(Regeste.objects.filter(pk=pk))
        serializer = RegesteSerializer(regeste)
        return Response(serializer.data)

