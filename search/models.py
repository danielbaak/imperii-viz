from django.db import models

# Create your models here.

class Search(models.Model):
    term = models.CharField(max_length=200)
    regest = models.CharField(max_length=200)
    occurences = models.IntegerField(null=True)


    def __unicode__(self):
        return '%d: %s' % (self.pk, self.name)


