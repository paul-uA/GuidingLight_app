

from  django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django.contrib.auth.models import User
from django import forms 
from django.forms import ModelForm
from main_app.models import GProfile, Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model= User
        fields = ['username','email','password1','password2']
        
class ProfileEdit(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model= User
        fields = ['username','email']        
        
class GProfileForm(ModelForm):
    class Meta:
        model = GProfile
        fields = ['bungiename', 'img', 'bio', 'bungieID', 'bungieIDLong', 'gamertag']
    
        widgets = {
            'bungiename' : forms.TextInput(),
            'img' : forms.TextInput(),
            'bio' : forms.Textarea(),
            'bungieID' : forms.TextInput(),
            'bungieIDLong' : forms.TextInput(),
            'gamertag' : forms.TextInput(),
        }
 