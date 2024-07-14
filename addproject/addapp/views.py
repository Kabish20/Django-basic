from django.shortcuts import render
from django.http import HttpResponse
def testing(request):
	a=30
	b=70
	c=a+b
	x='<h1>A value:'+str(a)+'B value:'+str(b)+'answer:'+str(c)+'</h1>'
	return HttpResponse(x)

# Create your views here.
