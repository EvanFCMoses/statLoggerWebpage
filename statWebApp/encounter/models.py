from django.db import models


class Disease(models.Model):
	disease_name = models.CharField(max_length = 50)
	stub_indicator = models.BooleanField(default = False)


class Encounter(models.Model):
	age = models.IntegerField(null=True)
	gender = models.CharField(max_length = 10, null=True)
	follow_up_status = models.CharField(max_length = 12, null=True)
	inpatient_outpatient_status = models.CharField(max_length = 12, null=True)
	latitude = models.IntegerField(null=True)
	longitude = models.IntegerField(null=True)
	date = models.DateField(null=True)
	notes = models.CharField(max_length = 1000, null=True)
	test_indicator = models.BooleanField(default = False)


class DiagnosisDiseaseGroupEntry(models.Model):
	disease_key = models.ForeignKey(Disease, on_delete = models.CASCADE)
	encounter_key = models.ForeignKey(Encounter, on_delete = models.CASCADE)
