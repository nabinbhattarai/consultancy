from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'main/home.html')

def about(request):
    return render(request,'main/about.html')

def contact(request):
    return render(request,'main/contact.html')

def service(request):
    return render(request,'main/services.html')

def ukcollege(request):
    return render(request,'main/ukcollege.html')

def uscollege(request):
    return render(request,'main/uscollege.html')

def cancollege(request):
    return render(request,'main/cancollege.html')

def auscollege(request):
    return render(request,'main/auscollege.html')