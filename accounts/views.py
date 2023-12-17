from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django import forms
from .models import Avatar
from accounts.forms import UserRegisterForm, UserUpdateForm, AvatarUpdateForm



def home(request):
    return  render(request, 'home.html')

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data

            usuario = data.get('username')
            contrasenia = data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user:
                login(request, user)

        return redirect('index')

    form = AuthenticationForm()
    contexto = {
        "form": form
    }
    return render(request, "login.html", contexto)


def register_request(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            is_admin = request.POST.get('is_admin')  # Asegúrate de que el campo is_admin está presente en tu formulario
            user.is_admin = is_admin
            user.save()
            login(request, user)
            return redirect("nombre_de_la_url_del_home")  # Reemplaza con la URL correcta de tu home

    form = UserRegisterForm()
    contexto = {
        "form": form
    }
    return render(request, "registrar.html", contexto)

@login_required
def editar_request(request):
    user = request.user
    if request.method == "POST":

        form = UserUpdateForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user.email = data["email"]
            user.last_name = data["last_name"]
            user.save()
            return redirect("index")

    form = UserUpdateForm(initial={"email": user.email, "last_name": user.last_name})
    contexto = {
        "form": form
    }
    return render(request, "registro.html", contexto)

def logout_view(request):
    logout(request)
    # Redirigir a la página que desees después del cierre de sesión
    return redirect('login')

@login_required
def editar_avatar_request(request):
    user = request.user
    if request.method == "POST":

        form = AvatarUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            try:
                avatar = user.avatar
                avatar.imagen = data["imagen"]
            except:
                avatar = Avatar(
                    user=user,
                    imagen=data["imagen"]
                )
            avatar.save()

            return redirect("index")

    form = AvatarUpdateForm()
    contexto = {
        "form": form
    }
    return render(request, "avatar.html", contexto)