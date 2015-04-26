from django.db import models

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

class Regeste(models.Model):
    title = models.CharField(max_length=150)
