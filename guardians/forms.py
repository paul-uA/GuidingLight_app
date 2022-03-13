from pyexpat import model
from  django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    
    class Meta:
        model= User
        field = ['username','first_name','last_name','email','password1','password2']