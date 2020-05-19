from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def world(request,pageid):
	if pageid == "0":
		return HttpResponse("safhe shomare sefr <a href='/'>Home</a>")
	else:
		return HttpResponse("404")