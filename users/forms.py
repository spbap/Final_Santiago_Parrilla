from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña',widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]
        
        help_text = {k: "" for k in fields}
        

class UserEditForm(UserChangeForm):
    password = None
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    imagen = forms.ImageField(label = "Avatar", required=False)
    
    class Meta:
        model = User
        fields = ["email","first_name","last_name","imagen"]

