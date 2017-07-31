# greetings/views.py
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hi Eugean! Remember to walk today :D")