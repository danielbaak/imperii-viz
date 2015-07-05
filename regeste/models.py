from django.db import models

from location.models import Location


class Department(models.Model):
    """
    Department id der uni mainz
    Department-->Volume-->Issue
    """
    name = models.CharField(max_length=200)
    department_id = models.IntegerField(unique=True)


class Volume(models.Model):
    """
    Volume id der uni mainz
    Department-->Volume-->Issue
    """
    volume_id = models.IntegerField()
    editor = models.CharField(max_length=200)
    department = models.ForeignKey('regeste.Department')

    class Meta:
        unique_together = ("volume_id", "department")


class Issue(models.Model):
    """
    Issue id der uni mainz
    Department-->Volume-->Issue
    """
    issue_id = models.IntegerField()
    volume = models.ForeignKey(Volume)

    class Meta:
        unique_together = ("issue_id", "volume")


class Regeste(models.Model):
    """
    Regeste mit allen informationen
    und ein link auf die uri von der uni mainz
    """
    title = models.CharField(max_length=150)
    issue = models.ForeignKey(Issue)
    place_of_issue = models.ForeignKey(Location, null=True, related_name='place_of_issue')
    issuer = models.ForeignKey('person.Person', related_name='regesten')
    issue_date = models.BigIntegerField(null=True)
    abstract = models.TextField(null=True)
    analysis = models.TextField(null=True) #Kommentare
    addenda = models.TextField(null=True) #Nachtragungen
    locations = models.ManyToManyField('location.Location', related_name='locations')
    people = models.ManyToManyField('person.Person', related_name='people')
    uni_mainz = models.ForeignKey('regeste.RegesteUniMainz')


class RegesteUniMainz(models.Model):
    """
    Uri der uni mainz für die api
    """
    uri = models.CharField(max_length=100)
    exchange = models.CharField(max_length=200)

    class Meta:
        unique_together = ("uri", "exchange")


