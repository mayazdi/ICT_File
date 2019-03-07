from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def default(request):
    return HttpResponse('<h1>This is heading</h1>')
