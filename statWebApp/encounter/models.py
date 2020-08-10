from django.db import models


class AgeRange(models.Model):
	primary_key = models.IntegerField(primary_key=true)
	lower_age_range = models.IntegerField()
	higher_age_range = models.IntegerField()
	range_text = models.CharField(max_length=50)


class Patient(models.Model):
	age = models.ForeignKey(AgeRange, on_delete = models.CASCADE)
	latitude = models.IntegerField()
	longitude = models.IntegerField()

class Disease(models.Model):
	primary_key = models.IntegerField(primary_key=true)
	disease_name = models.CharField(max_length = 50)

class Encounter(models.Model):
	patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
	diagnosis = models.ForeignKey(disease, on_delete = models.CASCADE)
	date = models.DateField()

# Create your models here.
