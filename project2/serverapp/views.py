from django.shortcuts import render
from django.http import HttpResponse
import datetime
def timefunction(request):
	date=datetime.datetime.now()
	s='<h1>CURRENT TIME IS:'+str(date)+'</h1>'
	return HttpResponse(s)

# Create your views here.
