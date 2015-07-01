from location.models import Location
from imperii_viz.celery import app


@app.task
def data_mining_regeste(regeste):
    if regeste.place_of_issue is None:
        search_for_loc(regeste)


def search_for_loc(regeste):
    words = regeste.abstract.split(" ")
    for word in words:
        locations = Location.objects.filter(name=word)
        if len(locations) >= 1:
            regeste.locations.add(locations.first())
            regeste.save()