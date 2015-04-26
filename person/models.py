from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=200)
    #e.g from wikipedia
    short_description = models.TextField()
    birth_date = models.DateField()
    death_date = models.DateField()
    gnd_number = models.IntegerField()
    #Foreign key in regeste
    #regesten = models.OneToManyField('Regeste')
