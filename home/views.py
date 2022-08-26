from django.shortcuts import render

# Create your views here.
def homeView(request):
    return render(request,'home/index.html')

def hrView(request):
    return render(request,'home/hr.html')

def legalView(request):
    return render(request,'home/legal.html')