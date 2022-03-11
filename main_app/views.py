from django.shortcuts import render
from django.views import View # class based "generic" view - from django - 
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView , ListView

from django.http import HttpResponse 
from .models import Profile , GameClass , JobPost 
from  .forms import PostForm
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


# ------------------ User Game Profile ---------------------

@ method_decorator (login_required, name='dispatch')  
class GamerProfile(TemplateView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = Profile.objects.get(user=self.request.user) # Here we are using the model to query the database for us.
        print(context)
        return context

class ProfileDetail(DetailView):
    model = Profile
    template_name = "profile_detail.html"    
    
class ProfileCreate(CreateView):
    model = Profile
    fields = ['bungiename', 'img', 'bio', 'bungieid', 'gamertag' ]
    template_name = 'Profile_create.html'
    success_url = '/profile/'

    # validate the form 
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProfileCreate, self).form_valid(form)

    # redirect 
    def get_success_url(self):
        return redirect('profile')

    
class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['bungiename', 'img', 'bio', 'bungieid', 'gamertag' ]
    template_name = 'profile_update.html'
    
    def get_success_url(self):
        # print(dir(self.object))
        return reverse('profile_detail', kwargs={'pk': self.object.pk})
 

class ProfileDelete(DeleteView):
    model = Profile
    template_name = "profile_delete_confirmation.html" #get - url 
    success_url = 'profile_create'


# ------------------ Game Class ----------------------------------

class GameClass(TemplateView):
    template_name = "class_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # to get the query parameter we have to acccess it in the request.GET dictionary object        
        name = self.reget("name")
        # If a query exists we will filter by name 
        if name != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
            context["artists"] = Artist.objects.filter(name__icontains=name)
        else:
            context["artists"] = Artist.objects.all()
        return context
    
    
class CreateClass(CreateView):
    model = GameClass
    fields = ['classtype', 'level', 'emblem']
    template_name = "class_create.html"
    success_url = "/profile/class/"


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
     form_class= PostForm
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
    
class Signup(View):
    
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form ssubmit validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile_create')
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)