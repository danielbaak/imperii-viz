from django.db import models
from .tasks import add_wiki_data_to_person
# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=200)
    #e.g from wikipedia
    short_description = models.TextField(null=True)
    birth_date = models.DateField(null=True)
    death_date = models.DateField(null=True)
    img_url = models.URLField(null=True)
    summary = models.TextField(null=True)
    gnd_number = models.IntegerField(null=True)

    def __str__(self):
        return '%d: %s' % (self.pk, self.name)

    def calculateMedian(self):
        count = self.regesten.count()
        return self.regesten.values_list().order_by('issue_date')[int(round(count/2))]

    def save(self, *args, **kwargs):
        super(Person, self).save(*args, **kwargs)
        add_wiki_data_to_person.delay(self)


