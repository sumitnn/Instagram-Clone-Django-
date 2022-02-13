from django import forms  
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()



class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields=['email','username','fullname','password1','password2']