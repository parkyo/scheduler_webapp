from django.shortcuts import render, redirect
from .models import RegisterForm

def registerView(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RegisterForm()    

    return render(request, 'register.html', {'form':form})