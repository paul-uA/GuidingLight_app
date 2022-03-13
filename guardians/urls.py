from re import template
from django import views
from django.urls import path
from .views import UserRegister, ProfileUpdate, ChangePassword, PasswordSuccess,ShowGProfile, EditGProfile
from django.contrib.auth import views as auth_views


# this like app.use() in express
urlpatterns = [
    path('register/', UserRegister.as_view(), name='register'),
    path('edit/', ProfileUpdate.as_view(), name='edit_profile'),
    path('password/', ChangePassword.as_view(template_name='registration/change_password.html')),
    path('password_success', PasswordSuccess ,name='password_success'),
    path('gprofile/<int:pk>',ShowGProfile.as_view(), name='show_gprofile' ),
    path('gprofile/<int:pk>/edit', EditGProfile.as_view(), name='edit_gprofile'),
 
#  path('profile/', views.GamerProfile.as_view(), name='profile'),
#  path('profile/new/', views.ProfileCreate.as_view(), name="profile_create"),
#  path('profile/<int:pk>/update',views.ProfileUpdate.as_view(), name="profile_update" ),
#  path('profile/<int:pk>/delete',views.ProfileDelete.as_view(), name="profile_delete"),
#  path('profile/class', views.GameClass.as_view(), name='gameclasses'),
#  path('profile/class/new/', views.CreateClass.as_view(), name="create_class"),
]