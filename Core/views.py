from django.shortcuts import render, HttpResponseRedirect
from .forms import RegistrationForm
from django.contrib import messages
from .models import User, ActiveUser

# Home
def home(request):
    users = ActiveUser.objects.all()
    return render(request, 'Core/home.html', {'users':users})

# About
def about(request):
    return render(request, 'Core/about.html')

# Contact
def contact(request):
    return render(request, 'Core/contact.html')

# Register
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulation!! You are registered')
            form.save()
    else:
        form = RegistrationForm()
    return render(request, 'Core/register.html', {'form': form})

# Faulters
def faulters(request):
    return render(request, 'Core/faulters.html')
