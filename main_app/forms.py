from django import forms
from .models import JobPost , ActivityType

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
            'bungieid' : forms.TextInput(attrs={'class': 'form-control'}),
            'activity_rank' : forms.TextInput(attrs={'class': 'form-control'})
            
        }
        