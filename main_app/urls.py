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
    # path('user/<int:pk>/', views.ArtistDetail.as_view(), name="artist_detail"),
    # path('clan', views.Clan.as_view(), name='clan'),
    # path('clan/<int:pk>/', views.ArtistDetail.as_view(), name="artist_detail"),
    # path('job-board', views.JobBoard.as_view(), name='JobBoard'),
    # path('job-board/<int:pk>/', views.ArtistDetail.as_view(), name="artist_detail"),
    #     
    # path('job-baord/<int:pk>/update', views.ArtistUpdate.as_view(), name="artist_update"),
    # path('job-board/<int:pk>/delete', views.ArtistDelete.as_view(), name="artist_delete"),
    # path('artists/<int:pk>/songs/new', views.SongCreate.as_view(), name="song_create"),
    # path('playlists/<int:pk>/songs/<int:song_pk>/', views.PlaylistSongAssoc.as_view(), name="playlist_song_assoc"),
    # our new view
    path('accounts/signup/', views.Signup.as_view(), name="signup")
    

] 