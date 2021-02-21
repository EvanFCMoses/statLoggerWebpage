from django.shortcuts import render
drom django.views import View

class Index(View):
	template = 'index.html'

	def get(self, request):
		return render(request, self.template)
