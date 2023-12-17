from django.contrib.auth.forms import UserCreationForm, User, CustomUser
from django import forms
from .models import Avatar


class CustomUserCreationForm(UserCreationForm):
    is_admin = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserRegisterForm(UserCreationForm, forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser  # Ajusta esto al modelo personalizado que estás utilizando
        fields = ("username", "email", "password1", "password2", "is_admin")