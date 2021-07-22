from django.db import models


class Disease(models.Model):
	disease_name = models.CharField(max_length = 50)
	stub_indicator = models.BooleanField(default = False)

	def __str__(self):
		return self.disease_name


class Encounter(models.Model):
	age = models.IntegerField(null=True)
	gender = models.CharField(max_length = 10, null=True)
	priorPatientStatus = models.CharField(max_length = 12, null=True)
	clinicLocation = models.CharField(max_length = 12, null=True)
	rolePlayed = models.CharField(max_length = 12, null=True)
	latitude = models.IntegerField(null=True, blank=True)
	longitude = models.IntegerField(null=True, blank=True)
	date = models.DateField(null=True)
	notes = models.CharField(max_length = 1000, null=True)
	test_indicator = models.BooleanField(default = False)

	def __str__(self):
		return str(self.date) + ' ' + self.clinicLocation + ' ' + self.notes


class DiagnosisDiseaseGroupEntry(models.Model):
	disease_key = models.ForeignKey(Disease, on_delete = models.CASCADE)
	encounter_key = models.ForeignKey(Encounter, on_delete = models.CASCADE)

	def __str__(self):
		return 'encounter #' + str(self.encounter_key.id)
