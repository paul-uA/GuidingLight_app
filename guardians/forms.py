

from  django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django.contrib.auth.models import User
from django import forms 
from django.forms import ModelForm
from main_app.models import GProfile, Profile

class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control-md'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control-md'}))
    
    class Meta:
        model= User
        fields = ['username','email','password1','password2']
        
class ProfileEdit(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control-md'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control-md'}))

    class Meta:
        model= User
        fields = ['username','email']        
        
class GProfileForm(ModelForm):
    class Meta:
        model = GProfile
        fields = ['bungiename', 'img', 'bio', 'bungieID', 'bungieIDLong', 'gamertag']
    
        widgets = {
            'bungiename' : forms.TextInput(attrs={'class': 'form-control-md'}),
            'img' : forms.TextInput(attrs={'class': 'form-control-md'}),
            'bio' : forms.Textarea(attrs={'class': 'form-control-md'}),
            'bungieID' : forms.TextInput(attrs={'class': 'form-control-md'}),
            'bungieIDLong' : forms.TextInput(attrs={'class': 'form-control-md'}),
            'gamertag' : forms.TextInput(attrs={'class': 'form-control-md'}),
        }
 