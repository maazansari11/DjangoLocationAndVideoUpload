import location as location
from django.db import models


# Create your models here.
class Location(models.Model):
    loc_id = models.IntegerField(primary_key=True)
    location_name = models.CharField(max_length=100)
    parent_id = models.IntegerField()
    description = models.CharField(max_length=500)
    longitude=models.DecimalField(max_digits=30, decimal_places=15)
    latitude= models.DecimalField(max_digits=30, decimal_places=15)


    def __str__(self):
        return 'loc_id={0}'.format(self.loc_id)


