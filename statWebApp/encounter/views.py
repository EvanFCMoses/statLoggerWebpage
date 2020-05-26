from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Location of encounter view.")
# Create your views here.
