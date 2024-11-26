from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def captain(request):
    return HttpResponse('<h1>KING KOHLI is captain of RCB</h1>')
def vicecaptain(request):
    return HttpResponse('<h1>FAF DU PLESSIS is vicecaptain of RCB</h1>')
