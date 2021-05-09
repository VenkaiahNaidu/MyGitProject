from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def hello(reqeust):
	return HttpResponse("welcome to django project ")

def venky(reqeust):
	return HttpResponse("this is my commit")
