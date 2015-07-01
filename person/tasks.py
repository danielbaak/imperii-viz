import wikipedia
from django.db.models.signals import  post_save
from django.dispatch import receiver
from imperii_viz.celery import app
from django.db.models import Avg
from regeste.models import Regeste
import datetime
import re
from itertools import chain

@app.task
def add_wiki_data_to_person(person):
        #TODO timo fragen ob schon fertig
        #print(wikipedia.search(self.name))
        #[u'Ford Motor Company', u'Gerald Ford', u'Henry Ford']
        wikipedia.set_lang("de")
        print("--------------")
        print(person.name)

        for entry in wikipedia.search(person.name, results=4):
            print(entry)
            avg_time = int(Regeste.objects.filter(issuer=person).aggregate(Avg("issue_date"))['issue_date__avg'])
            avg_year = datetime.datetime.fromtimestamp(int(avg_time)).year
            try:
                page_de = wikipedia.page(entry)
                wikipedia.set_lang("en")
                page_en = wikipedia.page(entry)
                wikipedia.set_lang("de")
                categories = page_de.categories
                for category in categories:
                    #todo search english and german
                    try:
                        regex_result = re.findall("Kategorie:Gestorben (\d+)|Kategorie:Geboren (\d+)|(\d+) births|(\d+) deaths", category)
                        search_results = list(filter(None, flatten(regex_result)))
                        for search_result in search_results:
                            if abs(int(search_result)-avg_year) <= 30:
                                if len(page_de.images) > 0:
                                    if page_de.images[0][-4:] == ".svg":
                                        person.img_url = page_de.images[1]
                                    else:
                                        person.img_url = page_de.images[0]
                                person.summary = page_de.summary

                                #person.death_date = datetime.date(search_result, 0, 0)
                                person.save()
                    except IndexError:
                        pass
            except wikipedia.exceptions.DisambiguationError:
                pass

        return


def flatten(list):
    "Flatten one level of nesting"
    return chain.from_iterable(list)