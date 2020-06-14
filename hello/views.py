from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def helloView(response):
    return render(response, 'main.html')