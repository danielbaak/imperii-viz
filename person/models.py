from django.db import models

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
