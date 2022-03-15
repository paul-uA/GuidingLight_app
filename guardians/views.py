
from ast import arg
from dataclasses import fields
from json import load
from multiprocessing import context
from pyexpat import model
from re import template
from webbrowser import get
from django.shortcuts import get_object_or_404, render
from django.views import View # class based "generic" view - from django - 
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView , ListView

from main_app.models import GProfile
from .forms import SignUpForm, ProfileEdit, GProfileForm

from django.http import HttpResponse 
from django.shortcuts import redirect, get_list_or_404
from django.urls import reverse, reverse_lazy

# import requests
# import os
# from dotenv import load_dotenv
# load_dorenv()

# imports related to signup
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm , UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView

# authorization decorators: 
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator    

class UserRegister(View):
    def get(self, request):
        form = SignUpForm
        context = {"form": form}
        return render(request, "registration/register.html", context)
    # on form ssubmit validate the form and login the user.
    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('create_gprofile')
        else:
            context = {"form": form}
            return render(request, "registration/register.html", context)

class ProfileUpdate(UpdateView):
        form_class = ProfileEdit
        template_name = 'registration/profile_update.html'
        success_url = reverse_lazy('home')
        def get_object(self):
            return self.request.user
    
class ChangePassword(PasswordChangeView):
    form_class =PasswordChangeForm
    success_url = reverse_lazy('password_success')
    
def PasswordSuccess(request):
    return render(request, 'registration/password_success.html',{})

class ShowGProfile(TemplateView):
    model = GProfile  
    template_name = 'registration/user_gprofile.html' 
    
    def get_context_data(self,*args ,**kwargs):
        context = super(ShowGProfile, self).get_context_data(*args,**kwargs)
        # print(GProfile.objects.filter(user=self.kwargs['pk']))
        user_info = GProfile.objects.get(user=self.kwargs['pk'])
        # print(type(user_info))
        context['user_info'] = user_info  
        print(context)  
        return context
    

class EditGProfile(UpdateView):  
    model = GProfile
    template_name= 'registration/edit_gprofile.html' 
    fields = [ 'bungiename', 'img','bio', 'bungieID','bungieIDLong', 'gamertag']
    success_url = reverse_lazy('home')


class CreateGProfile(CreateView):
    model= GProfile
    form_class = GProfileForm
    # fields = ['user','bungiename','img','bio','bungieID','bungieIDLong','gamertag']
    template_name = 'registration/create_gprofile.html'    
    success_url = reverse_lazy('home') 
    
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
     
# class GamerProfile(TemplateView):
#     template_name = "profile.html" 

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["profile"] = Profile.objects.get(user=self.request.user) # Here we are using the model to query the database for us.
#         print(context)
#         return context
    
# class ProfileCreate(CreateView):
#     model = Profile
#     fields = ['bungiename', 'img', 'bio', 'bungieid', 'gamertag' ]
#     template_name = 'Profile_create.html'
#     success_url = '/profile/'
