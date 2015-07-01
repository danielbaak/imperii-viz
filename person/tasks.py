import wikipedia
from django.db.models.signals import  post_save
from django.dispatch import receiver
from imperii_viz.celery import app
from django.db.models import Avg

@app.task
def add_wiki_data_to_person(person):
        #TODO timo fragen ob schon fertig
        #print(wikipedia.search(self.name))
        #[u'Ford Motor Company', u'Gerald Ford', u'Henry Ford']
        wikipedia.set_lang("de")
        print("--------------")
        print(person.name)

        for entry in wikipedia.search(person.name, results=4):
            avg_time = Regeste.objects.filter(issuer=p).aggregate(Avg("issue_date"))
            page = wikipedia.page(entry)

            #for regest in self.regesten:
            #    print(regest.issue_date)
        return