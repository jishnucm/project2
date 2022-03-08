from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('hai..')
    
def index2(request):
    return render(request,'index1.html')

def python(request):
    return render(request,'temp.html')    