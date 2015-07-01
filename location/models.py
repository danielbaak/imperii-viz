from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=20, decimal_places = 10)
    longitude = models.DecimalField(max_digits=20, decimal_places = 10)
    gnd_number = models.IntegerField(null=True)

    class Meta:
        unique_together = ("name", "latitude", "longitude")