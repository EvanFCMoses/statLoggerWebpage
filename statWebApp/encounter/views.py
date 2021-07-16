from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.template import loader
from .models import Disease
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
