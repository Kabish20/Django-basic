from django.shortcuts import render
from django.http import HttpResponse
from random import*
def testing(request):
	a=[10,20,30,40,50,60,70,80,90,100]
	result=choice(a)
	x='<h1> Random value is:....'+str(result)+'</h1>'
	return HttpResponse(x)

# Create your views here.
