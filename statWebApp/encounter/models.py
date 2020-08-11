from django.db import models


class AgeRange(models.Model):
	primary_key = models.IntegerField(primary_key = true)
	lower_age_range = models.IntegerField()
	higher_age_range = models.IntegerField()
	range_text = models.CharField(max_length=50)
	

class Disease(models.Model):
	primary_key = models.IntegerField(primary_key = true)
	disease_name = models.CharField(max_length = 50)

class PatientDiseaseGroup(models.Model):
	primary_key = modles.IntegerField(primary_key = true)

class DiagnosisDiseaseGroupEntry(models.Model):
	primary_key = models.IntegerField(primary_key)
	disease_key = models.ForeignKey(Disease, on_delete = models.CASCADE)
	patient_disease_group_key = models.ForeignKey(PatientDiseaseGroup, on_delete = models.CASCADE)


class Encounter(models.Model):
	age = models.ForeignKey(AgeRange, on_delete = models.CASCADE)
	gender = models.CharField(max_length = 10)
	follow_up_status = models.CharField(max_length = 12)
	inpatient_outpatient_status = models.CharField(max_length = 12)
	latitude = models.IntegerField()
	longitude = models.IntegerField()
	diagnosis = models.ForeignKey(DiagnosisDiseaseGroup, on_delete = models.CASCADE)
	date = models.DateField()
	notes = models.CharField(max_length = 1000)
	

# Create your models here.
