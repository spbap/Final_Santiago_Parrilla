from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, logout, login as auth_login
from users.forms import UserRegisterForm, UserEditForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .models import *

# Create your views here.

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data = request.POST)
        if form.is_valid():
            print("Datos validos!")
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            user = authenticate(username = usuario, password = contra)
            if user is not None:
                auth_login(request, user)
                return render(request,"app_final/home.html",{"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request,"users/login_error.html")
        else:
            return render(request,"users/login_error.html")
        
    form = AuthenticationForm()
    return render(request,"users/login.html")
    
def registro(request):
    msg_register = ""
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"users/registro_ok.html")
        else:
            msg_register = "Error en los datos ingresados"
        msg_register = "Error en los datos ingresados"
    form = UserRegisterForm()
     
    return render(request,"users/registro.html",{'form':form, "msg_register":msg_register})

def users_logout(request):
    logout(request)
    return render(request,'users/logout.html')

def editar_user(request):
    mensaje = ""
    usuario = request.user
    if request.method == "POST":
        miformulario = UserEditForm(request.POST, request.FILES, instance=usuario)
        if miformulario.is_valid():
            miformulario.save()
            if 'imagen' in request.FILES:
                if hasattr(usuario, 'avatar'):
                    usuario.avatar.imagen = request.FILES['imagen']
                    usuario.avatar.save()
                else:
                    Avatar.objects.create(user=usuario, imagen=request.FILES['imagen'])

            return render(request, "users/user_ok.html")
        else:
            mensaje = "Error al actualizar los datos"
    else:
        avatar_imagen = usuario.avatar.imagen.url if hasattr(usuario, 'avatar') and usuario.avatar.imagen else None
        miformulario = UserEditForm(initial={'imagen': avatar_imagen}, instance=usuario)

    return render(request, "users/editar_user.html", {"miformulario": miformulario,"usuario": usuario,"mensaje": mensaje})

class CambiarContra(LoginRequiredMixin,PasswordChangeView):
    template_name = 'users/cambiar_contra.html'
    success_url = reverse_lazy('user_ok')
    
def user_ok(request):
    return render(request,'users/user_ok.html')

