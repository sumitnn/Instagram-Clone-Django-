from django.shortcuts import render,redirect
from .forms import MyUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
import re
from core.models import User
# Create your views here.

def Login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user :
            login(request, user)
            messages.success(request,"Successfully Login")
            return redirect('home')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('login')
    return render(request,'authentication/signin.html')


def Signup(request):
    context={}
    if request.method == 'POST':
        forms=MyUserCreationForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('login')
        context['form']=forms
        return render(request,'authentication/signup.html',context)
    context['form']=MyUserCreationForm()
    return render(request,'authentication/signup.html',context)