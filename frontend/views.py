from django.shortcuts import render
from person.models import Person
# Create your views here.


def index_view(request):
    persons = Person.objects.all().order_by('img_url')
    return render(request, "frontend/index.html", {'persons': persons})