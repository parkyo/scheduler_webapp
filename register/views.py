from django.shortcuts import render, redirect
from .models import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def registerView(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('/login')
    else:
        form = RegisterForm()    

    return render(request, 'register.html', {'form':form})

