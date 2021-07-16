from django.db import models
	

class Disease(models.Model):
	primary_key = models.IntegerField(primary_key = True)
	disease_name = models.CharField(max_length = 50)
	stub_indicator = models.BooleanField(default = False)

class DiagnosisDiseaseGroupEntry(models.Model):
	primary_key = models.IntegerField(primary_key = True)
	disease_key = models.ForeignKey(Disease, on_delete = models.CASCADE)
	encounter_key = models.ForeignKey(Encounter, on_delete = models.CASCADE)


class Encounter(models.Model):
	age = models.IntegerField()
	gender = models.CharField(max_length = 10)
	follow_up_status = models.CharField(max_length = 12)
	inpatient_outpatient_status = models.CharField(max_length = 12)
	latitude = models.IntegerField()
	longitude = models.IntegerField()
	diagnosis = models.ForeignKey(DiagnosisDiseaseGroupEntry, on_delete = models.CASCADE)
	date = models.DateField()
	notes = models.CharField(max_length = 1000)
	test_indicator = models.BooleanField(default = False)