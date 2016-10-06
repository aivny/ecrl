from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse(u"This is the welcomePage.")

def home(request):
	return render(request,'Home.html')

def download(request):
	return render(request,'LinuxDownload.html')

def about(request):
	return render(request,'About.html')

def joinus(request):
	return render(request,'Joinus.html')

# Create your views here.
