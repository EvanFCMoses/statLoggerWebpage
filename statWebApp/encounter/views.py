from django.shortcuts import render
from django.views import View
import logging

class Index(View):
	template = 'index.html'

	def get(self, request):
		return render(request, self.template)


class DataEntry(View):
	template = 'dataEntry.html'

	def get(self, request):
		return render(request, self.template)


def process(request):
	logger = logging.getLogger('django')
	logger.debug('here is the request object fixify')
	for key in request:
		logger.debug('key: ' + key)
	return render(request, 'dataEntry.html')

