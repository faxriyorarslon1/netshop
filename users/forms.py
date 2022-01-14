from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class Register(UserCreationForm):
    email = forms.EmailField(widget = forms.EmailInput(attrs={"placeholder":"email"}))
    username = forms.CharField(widget = forms.TextInput(attrs={"placeholder":"username"}))
    password1 = forms.CharField(widget = forms.PasswordInput(attrs={"placeholder":"password"}))
    password2 = forms.CharField(widget = forms.PasswordInput(attrs={"placeholder":"re-password"}))


    class Meta:
        model = User
        fields=("email", "username", "password1", "password2")
    

class Login(AuthenticationForm):
    username = forms.CharField(widget = forms.TextInput(attrs={"placeholder":"username"}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={"placeholder":"password"}))

    class Meta:
        model = User
        fields=("username", "password")


