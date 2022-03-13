from re import template
from venv import create
from django.shortcuts import render
from django.views import View # class based "generic" view - from django - 
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView , ListView
from .forms import UserCreationForm

from django.http import HttpResponse 
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy

# imports related to signup
from django.contrib.auth import login
# from django.contrib.auth.forms import UserCreationForm

# authorization decorators: 
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator    

class UserRegister(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/register.html", context)
    # on form ssubmit validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
        else:
            context = {"form": form}
            return render(request, "registration/register.html", context)
        
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
