from django.db import models
from django.contrib.auth.models import User


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
        return self.bungiename

    class Meta:
        ordering = ['bungiename']
        
        
class GameClass(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    classtype = models.CharField(max_length=10)
    level = models.IntegerField(default=1350)
    emblem = models.CharField(max_length=500)
    
    
    def __str__(self):
        return self.classtype
  

class GamePost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bungieid = models.CharField(max_length=100)
    activity_name = models.CharField(max_length=200)
    activity_rank = models.CharField(max_length=150)
    
class JobPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bungieid = models.CharField(max_length=100)
    activity_name = models.CharField(max_length=200)
    activity_rank = models.CharField(max_length=150)