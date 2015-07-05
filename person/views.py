from person.serializers import PersonSerializer
from person.models import Person
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from regeste.models import Regeste
from regeste.serializers import RegesteSerializer

class PersonView(APIView):
    def get(self, request, format=None):
        events = Person.objects.all().order_by('img_url')
        serializer = PersonSerializer(events, many = True)
        return Response(serializer.data)

class PersonDetail(APIView):

    def get(self, request, pk, format=None):
        person = get_object_or_404(Person.objects.filter(pk=pk))
        serializer = PersonSerializer(person)
        return Response(serializer.data)


@api_view(['GET'])
def regentenList(request, person_id, format=None):
    person = get_object_or_404(Person.objects.filter(pk=person_id))
    regesten = Regeste.objects.filter(issuer=person)
    serializer = RegesteSerializer(regesten, many=True)
    return Response(serializer.data)


