from django.shortcuts import render
from django.views import View
from .models import Disease, Encounter, DiagnosisDiseaseGroupEntry
from datetime import date
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

		return returnDataEntry(request)

	elif request.method == 'GET':
		return returnDataEntry(request)

def returnDataEntry(request):
	all_diseases = Disease.objects.all()
	context = {'all_diseases': all_diseases,}
	return render(request, 'dataEntry.html', context)

class SavePost():

	def addDiagnosis(self, encounter, diagnosis):
		newDiagnosis, created = Disease.objects.get_or_create(disease_name=str(diagnosis).strip(), stub_indicator=True)
		newDiagnosis.save()
		diagnosisLookupTable = DiagnosisDiseaseGroupEntry(disease_key=newDiagnosis, encounter_key=encounter)
		diagnosisLookupTable.save()

	def processAndSaveNewEntry(self, message):
		logger = logging.getLogger('django')

		encounter = Encounter()
		encounter.save()
		for key, value in message.items():
			if key == "gender":
				encounter.gender = str(value)
			elif key == "patientAge":
				encounter.age = int(value)
			elif key == "clinicLocation":
				encounter.clinicLocation = str(value)
			elif key == "priorPatient":
				encounter.priorPatientStatus = str(value)
			elif key == "rolePlayed":
				encounter.rolePlayed = str(value)
			elif key == "notes":
				encounter.notes = str(value)
			elif "maladies" in key:
				self.addDiagnosis(encounter, value)
		encounter.date = date.today()
		encounter.save()
