from location.models import Location
from imperii_viz.celery import app


@app.task
def data_mining_regeste(regeste):
    try:
        search_for_loc(regeste)
    except Location.DoesNotExist:
        pass


def search_for_loc(regeste):
    regeste.save()
    words = regeste.abstract.split(" ")
    for word in words:
        locations = Location.objects.filter(name=word)
        if len(locations) >= 1:
            regeste.locations.add(locations.first())
            regeste.save()