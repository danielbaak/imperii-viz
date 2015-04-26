from django.db import models
from person.models import Person
from location.models import Location
# Create your models here.
# Personen
# -Name
# -short_description
# -birth_date
# -death_date
# Regeste
# -Person
# -Inhalt
# -Datum
# -Ort
# Orte
# Portrais
#


class Department(models.Model):
    name = models.CharField(max_length=200)
    department_id = models.IntegerField(unique=True)


class Volume(models.Model):
    volume_id = models.IntegerField()
    editor = models.CharField(max_length=200)
    department = models.ForeignKey(Department)

    class Meta:
        unique_together = ("volume_id", "department")


class Issue(models.Model):
    issue_id = models.IntegerField()
    volume = models.ForeignKey(Volume)

    class Meta:
        unique_together = ("issue_id", "volume")


class Regeste(models.Model):
    title = models.CharField(max_length=150)
    issue = models.ForeignKey(Issue)
    place_of_issue = models.ForeignKey(Location)
    issuer = models.ForeignKey(Person)
    issue_date = models
    abstract = models.TextField()
    analysis = models.TextField() #Kommentare
    addenda = models.TextField() #Nachtragungen
    uni_mainz = models.ForeignKey('RegesteUniMainz')


class RegesteUniMainz(models.Model):
    uri = models.CharField(max_length=100)
    exchange = models.CharField(max_length=200)


