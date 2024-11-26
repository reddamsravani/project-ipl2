from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def captain(request):
    return HttpResponse('<h1>Ruturaj is captain of CSK</h1>')
def vicecaptain(request):
    return HttpResponse('<h1>jadija is vice captain of CSK</h1>')
