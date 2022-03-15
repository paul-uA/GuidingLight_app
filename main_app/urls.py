from django.urls import path
from . import views 


# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('how-to-use/', views.HowTo.as_view(), name="howto"), # <- new route
    path('jobboard/', views.ListsPost.as_view(), name='gamepost_list'),
    path('jobboard/<int:pk>/', views.JobDetail.as_view(), name="job_detail"),
    path('jobboard/new', views.NewJobPost.as_view(), name="jobpost_create"),
    path('jobboard/<int:pk>/update', views.UpdateJob.as_view(), name="jobpost_update"),
    path('jobboard/<int:pk>/delete', views.DeleteJob.as_view(), name="jobpost_delete"),
    path('jobboard/<str:cat>', views.CatergoryView, name='jb_catergory'),
    # path('user/<int:pk>/', views.ArtistDetail.as_view(), name="artist_detail"),
    # path('clan', views.Clan.as_view(), name='clan'),
    # path('clan/<int:pk>/', views.ArtistDetail.as_view(), name="artist_detail"),
    # path('accounts/signup/', views.Signup.as_view(), name="signup")
    

] 