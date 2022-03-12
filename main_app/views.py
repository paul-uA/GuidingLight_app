from django.shortcuts import render
from django.views import View # class based "generic" view - from django - 
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView , ListView

from django.http import HttpResponse 
from .models import Profile , GameClass , JobPost 
# from  .forms import PostForm
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy

# imports related to signup
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# authorization decorators: 
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator    

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"
       

class HowTo(TemplateView):  
    template_name = "howtouse.html"



# ---------------------------Job Board stuff ---------------------------------------

class ListsPost(ListView):
    model = JobPost
    template_name="post_list.html"
    ordering= ['-date_created']

class JobDetail(DetailView):
    model = JobPost
    template_name="jobpost_detail.html"
    
class NewJobPost(CreateView):
     model= JobPost
    #  form_class= PostForm
     template_name= "new_jobpost.html"  
     fields= '__all__' 
     
class UpdateJob(UpdateView):
    model = JobPost
    template_name = 'update_job.html'
    fields=['activity_name','activity_rank']

class DeleteJob(DeleteView):
    model= JobPost    
    template_name = 'delete_jobpost.html'
    success_url = reverse_lazy('gamepost_list')
#------------ Auth Views ---------------------------- 
    
# class Signup(View):
    
    # show a form to fill out
    # def get(self, request):
    #     form = UserCreationForm()
    #     context = {"form": form}
    #     return render(request, "registration/signup.html", context)
    # # on form ssubmit validate the form and login the user.
    # def post(self, request):
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         login(request, user)
    #         return redirect('profile_create')
    #     else:
    #         context = {"form": form}
    #         return render(request, "registration/signup.html", context)