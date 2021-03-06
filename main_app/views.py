
from django.shortcuts import render
from django.views import View # class based "generic" view - from django - 
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView , ListView

from django.http import HttpResponse 
from .models import ActivityType, Profile , GameClass , JobPost, Comment 
from  .forms import PostForm, CommentForm
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
    template_name="post_list.html"
    model = JobPost
    ordering= ['-date_created']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["jobpost"] = JobPost.objects.all().order_by('-date_created') # Here we are using the model to query the database for us.
        context['category']= ActivityType.objects.all()
        # print(context)
        return context
 
@method_decorator(login_required, name="dispatch")    
class AddComment(CreateView):
     model= Comment
     form_class= CommentForm
     template_name= "add_comment.html"  
    #  fields= ['activity_name','activity_rank','bungieid', 'notes', 'category'] 
     success_url= reverse_lazy('gamepost_list')     
     
     def form_valid(self, form):
         print(self.kwargs) 
         form.instance.post_id= self.kwargs['pk']
         return super().form_valid(form) 

class JobDetail(DetailView):
    model = JobPost
    template_name="jobpost_detail.html"
    
    
    
@method_decorator(login_required, name="dispatch")    
class NewJobPost(CreateView):
     model= JobPost
     form_class= PostForm
     template_name= "new_jobpost.html"  
    #  fields= ['activity_name','activity_rank','bungieid', 'notes', 'category'] 
    
     def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NewJobPost, self).form_valid(form)
    
@method_decorator(login_required, name="dispatch")     
class UpdateJob(UpdateView):
    model = JobPost
    template_name = 'update_job.html'
    fields=['activity_name','activity_rank']

@method_decorator(login_required, name="dispatch")
class DeleteJob(DeleteView):
    model= JobPost    
    template_name = 'delete_jobpost.html'
    success_url = reverse_lazy('gamepost_list')
    
def CatergoryView(request,cat):
    cat = cat
    print(cat)
    jb_cat = ActivityType.objects.filter(name=cat)
    print(jb_cat)
    if not jb_cat :
        return render(request,'bad_url.html')
    else:  
        ids = jb_cat.values_list('pk', flat=True)
        print(ids[0])
        category_post = JobPost.objects.filter(category=ids[0]).order_by('-date_created')
        return render(request, 'jb_catergories.html',{'cat':cat,'category_post': category_post }) #'category_post': category_post    
    
# ---------------------------Job Board stuff --------------   

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