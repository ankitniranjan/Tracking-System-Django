from django.shortcuts import render, HttpResponseRedirect
from .forms import RegistrationForm
from django.contrib import messages
from .models import User, ActiveUser

# Home
def home(request):
    users = ActiveUser.objects.all()
    state = 'active'
    return render(request, 'Core/home.html', {'users':users, 'hstate':state})

# About
def about(request):
    state = 'active'
    return render(request, 'Core/about.html', {'astate':state})

# Contact
def contact(request):
    state = 'active'
    return render(request, 'Core/contact.html', {'cstate':state})

# Register
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulation!! You are registered')
            form.save()
    else:
        form = RegistrationForm()
    state = 'active'
    return render(request, 'Core/register.html', {'form': form, 'rstate':state})

# Faulters
def faulters(request):
    users = ActiveUser.objects.all()
    state = 'active'
    return render(request, 'Core/faulters.html', {'users': users, 'fstate':state})
