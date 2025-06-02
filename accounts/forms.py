from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=UserProfile.ROLE_CHOICES, initial='student')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']