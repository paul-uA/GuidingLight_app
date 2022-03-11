from django.contrib import admin

# Register your models here.
from .models import Profile , GameClass, JobPost # import the Artist model from models.py
# Register your models here.

admin.site.register(Profile) # this line will add the model to the admin panel
admin.site.register(GameClass)
admin.site.register(JobPost)