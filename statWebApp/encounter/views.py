from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.template import loader
from .models import Disease, Encounter, DiagnosisDiseaseGroupEntry
import logging

class Index(View):
	template = 'index.html'

	def get(self, request):
		return render(request, self.template)


def dataEntry(request):
	if request.method == 'POST':
		logger = logging.getLogger('django')
		logger.debug('here is the request object fixify')
		logger.debug('keys:')
		message = request.POST
		processAndSaveNewEntry(message.items)
		for key, value in message.items():
			logger.debug(key)
			logger.debug(value)

		return returnDataEntry(request)
	
	elif request.method == 'GET':
		return returnDataEntry(request)

def returnDataEntry(request):
	all_diseases = Disease.objects.all()
	template = loader.get_template('dataEntry.html')
	context = {
		'all_diseases': all_diseases,
	}
	return HttpResponse(template.render(context, request))

class savePost(self):
	def updateGender(encounter, gender):
		encounter.gender = gender
	def updatePatientAge(encounter, patientAge):
		encounter.patientAge = patientAge
	def updateClinicLocation(encounter, clinicLocation):
		encounter.clinicLocation = clinicLocation
	def updatePriorPatient(encounter, priorPatient):
		encounter.priorPatient = priorPatient
	def updateRolePlayed(encounter, rolePlayed):
		encounter.rolePlayed = rolePlayed
	def updateNotes(encounter, notes):
		encounter.notes = notes
	def addDiagnosis(encounter, diagnosis):
		newDiagnosis, created = Disease.objects.get_or_create(disease_name=diagnosis, stub_indicator=True) #FIXIFY stubRemoval
		newDiagnosis.save()
		diagnosisLookupTable = DiagnosisDiseaseGroupEntry(disease_key=newDiagnosis, encounter_key=encounter)
		diagnosisLookupTable.save()

	inputMap = {
		"gender":updateGender,
		"patientAge":updatePatientAge,
		"clinicLocation":updateClinicLocation,
		"priorPatient":updatePriorPatient,
		"rolePlayed":updateRolePlayed,
		"notes":updateNotes,
	}	

	def processAndSaveNewEntry(messageItems):
		encounter = Encounter()
		for key, value in messageItems:
			if key in inputMap:
				func = inputMap.get(key, "nothing")
				func(encounter, value)
			else:
				addDiagnosis(encounter, value)

