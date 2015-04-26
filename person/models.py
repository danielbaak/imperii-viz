from django.db import models
from regeste.models import Regeste
import wikipedia
# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=200)
    #e.g from wikipedia
    short_description = models.TextField(null=True)
    birth_date = models.DateField(null=True)
    death_date = models.DateField(null=True)
    gnd_number = models.IntegerField(null=True)

    def __str__(self):
        return '%d: %s' % (self.pk, self.name)

    def addWikiDataToPerson(self):
        #print(wikipedia.search(self.name))
        #[u'Ford Motor Company', u'Gerald Ford', u'Henry Ford']
        for entry in wikipedia.search(self.name, results=4):
            print(entry)
            #for regest in self.regesten:
            #    print(regest.issue_date)


    def calculateMedian(self):
        count = self.regesten.count()
        return self.regesten.values_list().order_by('issue_date')[int(round(count/2))]