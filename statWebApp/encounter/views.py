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

	def post(self, request):
		logger = logging.getLogger('django')
		logger.debug('here is the request object fixify')
		logger.debug('keys:')
		message = request.POST
		for key, value in message.items():
			logger.debug(key)
			logger.debug(value)
		return render(request, 'dataEntry.html')


# def process(request):
# 	logger = logging.getLogger('django')
# 	logger.debug('here is the request object fixify')
# 	logger.debug('keys:')
# 	message = request.POST
# 	for key, value in message.items():
# 		logger.debug(key)
# 		logger.debug(value)
# 	return render(request, 'dataEntry.html')

