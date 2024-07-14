from django.shortcuts import render
from django.http import HttpResponse
def myfunction(request):
	s='<html><body bgcolor="blue"><h1><font color="white">its present of problem</font></h1></body></html>'
	return HttpResponse(s)

# Create your views here.
