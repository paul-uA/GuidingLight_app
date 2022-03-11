from django import forms
from .models import JobPost

class PostForm(forms.Form):
    class Meta:
        model = JobPost
        fields = ('activity_name' , 'activity_rank', 'bungieid')
        
        widgets = {
            'activity_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'bungieid' : forms.TextInput(attrs={'class': 'form-control'}),
            'activity_rank' : forms.TextInput(attrs={'class': 'form-control'}),
            
        }
        