from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def sanny(request):
    return HttpResponse('sanny is my friend')