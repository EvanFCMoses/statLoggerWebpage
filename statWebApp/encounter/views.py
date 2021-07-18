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
		message = request.POST
		savePost = SavePost()
		savePost.processAndSaveNewEntry(message)
#		logger = logging.getLogger('django')
#		for key, value in message.items():
#			logger.debug(key)
#			logger.debug(value)

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

class SavePost():
	def updateGender(encounter, gender):
		encounter.gender = str(gender)
		encounter.save()
	def updatePatientAge(encounter, patientAge):
		encounter.patientAge = str(patientAge)
		logger = logging.getLogger('debug')
		logger.debug('after saving patient age')
		logger.debug(encounter)
		encounter.save()
	def updateClinicLocation(encounter, clinicLocation):
		encounter.clinicLocation = str(clinicLocation)
		encounter.save()
	def updatePriorPatient(encounter, priorPatient):
		encounter.priorPatient = str(priorPatient)
		encounter.save()
	def updateRolePlayed(encounter, rolePlayed):
		encounter.rolePlayed = str(rolePlayed)
		encounter.save()
	def updateNotes(encounter, notes):
		encounter.notes = str(notes)
		encounter.save()
	def addDiagnosis(self, encounter, diagnosis):
		newDiagnosis, created = Disease.objects.get_or_create(disease_name=str(diagnosis).strip(), stub_indicator=True) #FIXIFY stubRemoval
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

	def processAndSaveNewEntry(self, message):
#		logger = logging.getLogger('django')

		encounter = Encounter()
		encounter.save()
		for key, value in message.items():
			if key in self.inputMap:
#				logger.debug("key: " + str(key))
				func = self.inputMap.get(key, "nothing")
#				logger.debug("func: " + str(func))
				func(encounter, value)
			elif "maladies" in key:
				self.addDiagnosis(encounter, value)
		encounter.save()
