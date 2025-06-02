# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import UserRegistrationForm, UserLoginForm
from .models import UserProfile


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Update the user's role
            user_profile = user.userprofile
            user_profile.role = form.cleaned_data['role']
            user_profile.save()

            messages.success(request, 'Registration successful. You are now logged in.')
            login(request, user)
            return redirect('core:home')
    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('core:home')
    else:
        form = UserLoginForm()

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('core:home')