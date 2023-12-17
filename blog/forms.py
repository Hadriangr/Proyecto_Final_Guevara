
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Avatar,Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'titulo', 'subtitulo', 'contenido']
        
class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario', max_length=100)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    
    
class CustomUserCreationForm(UserCreationForm):
    is_admin = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserRegisterForm(CustomUserCreationForm, forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("username", "email")


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', "last_name")


class AvatarUpdateForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ("imagen",)
