from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class Incidences(models.Model):
    name = models.CharField(max_length=200)
    location = models.PointField(max_length=20)
    #objects = GeoManager()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Incidences"
