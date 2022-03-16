from dataclasses import fields
from pyexpat import model
from django import forms
from .models import JobPost , ActivityType, Comment

# choices = ActivityType.objects.all().values_list('name', 'name')
# choice_list=[]
# for item in choices:
#     choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = JobPost
        fields = ('activity_name','activity_rank', 'bungieid','notes','category')
        
        widgets = {
            'activity_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'bungieid' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' :"Bungie#7777"}),
            'activity_rank' : forms.TextInput(attrs={'class': 'form-control'}),
            'notes' : forms.Textarea(attrs={'class': 'form-control'})
            
            
        }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields= ('username','body')
        
        widgets = {
            'username' : forms.TextInput(attrs={'class': 'form-control-md'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),
        }