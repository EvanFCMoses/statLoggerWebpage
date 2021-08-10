from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Disease, Encounter, DiagnosisDiseaseGroupEntry
from datetime import date
import logging

class Index(View):
	template = 'index.html'

	def get(self, request):
		return render(request, self.template)

@login_required(login_url='/encounter/login/')
def dataEntry(request):
	logger = logging.getLogger('django')
	if request.method == 'POST':
		message = request.POST
		savePost = SavePost(message)
		logger.debug('fixify savePost.checkInput: ' + str(savePost.checkInput()))
		logger.debug('fixify savePost.getMissinginfo: ' + str(savePost.getMissingEnteredData()))
		logger.debug('fixify savePost.checkForMaladies: ' + str(savePost.checkForMaladies()))
		if savePost.checkInput():
			savePost.processAndSaveNewEntry()
			return returnDataEntry(request)

		else:
			return returnDataEntryWithError(request, savePost.getMissingEnteredData())

	elif request.method == 'GET':
		return returnDataEntry(request)

def returnDataEntry(request):
	all_diseases = Disease.objects.all()
	context = {'all_diseases': all_diseases,}
	return render(request, 'dataEntry.html', context)

def returnDataEntryWithError(request, missingEnteredData):
	all_diseases = Disease.objects.all()
	context = {
	'all_diseases': all_diseases,
	'incompleteDataEntered': missingEnteredData,
	}
	return render(request, 'dataEntry.html', context)

def loginDataEntry(request):
	logger = logging.getLogger('django')
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('/encounter/')
	return render(request, 'login.html')

class SavePost():

	message = ""
	minimumInput = ('gender', 'clinicLocation', 'priorPatient')

	def __init__(self, message):
		self.message=message

	def checkInput(self):
		if len(self.getMissingEnteredData()) == 0:
			return True
		return False


	def addDiagnosis(self, encounter, diagnosis):
		newDiagnosis, created = Disease.objects.get_or_create(disease_name=str(diagnosis).strip(), stub_indicator=True)
		newDiagnosis.save()
		diagnosisLookupTable = DiagnosisDiseaseGroupEntry(disease_key=newDiagnosis, encounter_key=encounter)
		diagnosisLookupTable.save()

	def processAndSaveNewEntry(self):
		logger = logging.getLogger('django')

		logger.debug('fixify saving the post')

		encounter = Encounter()
		encounter.save()
		for key, value in self.message.items():
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

	def checkForMaladies(self):
		for key in self.message.keys():
			if 'maladies' in key:
				return True
		return False

	def getMissingEnteredData(self):
		missingKeys = []

		for minimumKey in self.minimumInput:
			if minimumKey not in self.message.keys():
				missingKeys.append(minimumKey)

		if(self.message.get('patientAge','') == ''):
			missingKeys.append('patientAge')

		if(not self.checkForMaladies()):
			missingKeys.append('diagnosis')

		return missingKeys
