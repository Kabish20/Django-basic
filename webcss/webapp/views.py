from django.shortcuts import render
from django.http import HttpResponse
from datetime import *
def test(request):
	today=datetime.now()
	x='<h1>Today Is: '+str(today.strftime("%d-%m-%y"))+'</h1>'
	return HttpResponse(x)

# Create your views here.
