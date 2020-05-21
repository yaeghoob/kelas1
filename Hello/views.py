from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("hello, welcome to my site, <a href='/about'>about</a><a href='/pages'>pages</a>	")
	


def about(request):
	return HttpResponse("i am.. <a href='/'>Go TO Home</a> ") 


def pages(request):
	return HttpResponse("page1 , page2, page3")


def page(request,pageid):

	return HttpResponse("page<?p{pageid}>")