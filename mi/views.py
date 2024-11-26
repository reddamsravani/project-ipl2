from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def captain(request):
    return HttpResponse('<h1>HARDIK PANDYA is captain of mi</h1>')
def vicecaptain(request):
    return HttpResponse('<h1>ROHIT is vice captain of mi</h1>')

