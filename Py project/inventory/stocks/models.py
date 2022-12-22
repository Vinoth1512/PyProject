from django.db import models

# Create your models here.
class Location(models.Model):
    location_name = models.CharField(max_length=255,null=True,blank=True)
    description = models.CharField(max_length=255,null=True,blank=True)

    class Meta:
        db_table = 'stocks_location'

class Company(models.Model):
    company_name = models.CharField(max_length=255,null=True,blank=True)
    description = models.CharField(max_length=255,null=True,blank=True)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE,db_column='location_id')

    class Meta:
        db_table = 'stocks_company'


