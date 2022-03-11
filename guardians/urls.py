from django.urls import path
from . import views


# this like app.use() in express
urlpatterns = [
 
 path('profile/', views.GamerProfile.as_view(), name='profile'),
 path('profile/new/', views.ProfileCreate.as_view(), name="profile_create"),
 path('profile/<int:pk>/update',views.ProfileUpdate.as_view(), name="profile_update" ),
 path('profile/<int:pk>/delete',views.ProfileDelete.as_view(), name="profile_delete"),
 path('profile/class', views.GameClass.as_view(), name='gameclasses'),
 path('profile/class/new/', views.CreateClass.as_view(), name="create_class"),
]