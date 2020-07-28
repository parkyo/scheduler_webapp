# from django.contrib.auth.models import user
from django.shortcuts import render

# Create your views here.

def loginView(response):
    return render(response, 'login.html')