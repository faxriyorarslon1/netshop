from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import Register, Login
from django.contrib.auth.forms import AuthenticationForm


from django.contrib.auth import authenticate, login 

def register(request):
    form_r = Register()
    form_l = Login()
    if request.method == "POST":
        form_r = Register(request.POST)
        form_l = AuthenticationForm(request, request.POST)
        if form_r.is_valid():
            form_r.save()
            return redirect('/')
        if form_l.is_valid():
            username = form_l.cleaned_data.get('username')
            password = form_l.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')

    
    context = { 'form_r':form_r,
                'form_l':form_l}
    
    return render(request, template_name='login.html', context=context)


def logout_view(request):
    logout(request)
    # return render(request,'index.html')
    return redirect('/')