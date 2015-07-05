from django.db import models
from .tasks import add_wiki_data_to_person


class Person(models.Model):
    """model to represent a historic figure"""
    name = models.CharField(max_length=200, unique=True)
    short_description = models.TextField(null=True)
    birth_date = models.DateField(null=True)
    death_date = models.DateField(null=True)
    img_url = models.URLField(null=True)
    gnd_number = models.CharField(max_length=200, null=True)

    def __str__(self):
        return '%d: %s' % (self.pk, self.name)

    def save(self, *args, **kwargs):
        super(Person, self).save(*args, **kwargs)
        add_wiki_data_to_person.delay(self)


