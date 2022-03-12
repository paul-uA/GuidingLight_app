from django.db import models

# Create your models here.
# class Profile(models.Model):
#     bungiename = models.CharField(max_length=100,default='BungieID#1111', editable=True, unique=True)
#     img = models.CharField(max_length=500)
#     bio = models.TextField(max_length=500)
#     bungieid = models.CharField(max_length=100)
#     gamertag = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)
#     # Here is our new column
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.bungiename

#     class Meta:
#         ordering = ['bungiename']
        
        