
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.urls import reverse

from django.db.models.signals import post_save
from django.dispatch import receiver




# Create your models here.

class Profile(models.Model):
    bungiename = models.CharField(max_length=100,default='BungieID#1111', editable=True, unique=True)
    img = models.CharField(max_length=500)
    bio = models.TextField(max_length=500)
    bungieid = models.CharField(max_length=100)
    gamertag = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    # Here is our new column
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user

    class Meta:
        ordering = ['bungiename']

class GProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bungiename = models.CharField(max_length=100,default='BungieID#1111', editable=True, unique=True)
    img = models.CharField(max_length=500, default='https://www.bungie.net/img/profile/avatars/bungie_day_15_29.jpg')
    bio = models.TextField(max_length=500)
    bungieID = models.CharField(max_length=100)
    bungieIDLong = models.CharField(max_length=100)
    gamertag = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    # Here is our new column

    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):
        return reverse('show_gprofile', kwargs={'pk':self.pk})   
        
class GameClass(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    classtype = models.CharField(max_length=10)
    level = models.IntegerField(default=1350)
    emblem = models.CharField(max_length=500)
    
    
    def __str__(self):
        return self.classtype
  
class ActivityType(models.Model):
    name= models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('job_detail', kwargs={'pk':self.pk})
    
class JobPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    bungieid = models.CharField(max_length=100)
    activity_name = models.CharField(max_length=200)
    activity_rank = models.CharField(max_length=150)
    notes = models.TextField(max_length=500)
    category = models.ForeignKey(ActivityType, on_delete=models.CASCADE)
    
    
    
    def __str__(self):
        return self.activity_name + " | " + str(self.user)
    
    def get_absolute_url(self):
        return reverse('job_detail', kwargs={'pk':self.pk})

class Comment(models.Model):
    post = models.ForeignKey(JobPost, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    username = models.CharField(max_length=150)
    created= models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    
    class Meta:
        ordering= ['created']
    
    def __str__(self):
        return f'Comment by {self.username} on {self.post}'
        

           