import wikipedia
from imperii_viz.celery import app
from django.db.models import Avg
from regeste.models import Regeste
import datetime
import re
from itertools import chain


@app.task
def add_wiki_data_to_person(person):
    """function to mine data from a wikipedia page and save it to the person object"""
    wikipedia.set_lang("de")
    for entry in wikipedia.search(person.name, results=4):
        avg_time = int(Regeste.objects.filter(issuer=person).aggregate(Avg("issue_date"))['issue_date__avg'])
        avg_year = datetime.datetime.fromtimestamp(int(avg_time)).year
        try:
            page_de = wikipedia.page(entry)
            categories = page_de.categories
            for category in categories:
                try:
                    regex_result = re.findall("Kategorie:Gestorben (\d+)|Kategorie:Geboren (\d+)", category)
                    search_results = list(filter(None, flatten(regex_result)))
                    for search_result in search_results:
                        if abs(int(search_result)-avg_year) <= 30:
                            if len(page_de.images) > 0:
                                if page_de.images[0][-4:] == ".svg":
                                    person.img_url = page_de.images[1]
                                else:
                                    person.img_url = page_de.images[0]
                            person.short_description = page_de.summary
                            person.save()
                except IndexError:
                    pass
        except wikipedia.exceptions.DisambiguationError and wikipedia.exceptions.PageError:
            pass
    return


def flatten(list):
    """Flatten one level of nesting"""
    return chain.from_iterable(list)