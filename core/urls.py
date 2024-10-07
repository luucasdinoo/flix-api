from django.contrib import admin
from django.urls import path
from app_genres.views import GenreCreateListView, GenreRetrievelUpdateDestroyView
from app_actors.views import ActorCreateListView, ActorRetrieveUpdateDestroyView
from app_movies.views import MovieCreateListView, MovieRetrievelUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('genres/', GenreCreateListView.as_view() , name='genre-create-list'),
    path('genres/<int:pk>', GenreRetrievelUpdateDestroyView.as_view(),                        name='genre-update-detail-destroy'),
    
    path('actors/', ActorCreateListView.as_view(), name= 'actor-create-list'),
    path('actors/<int:pk>/', ActorRetrieveUpdateDestroyView.as_view(), 
    name= 'actor-update-detail-destroy'),
    
    path('movies/', MovieCreateListView.as_view(), name= 'movie-create-list'),
    path('movies/<int:pk>/', MovieRetrievelUpdateDestroyView.as_view(), 
    name= 'movie-update-detail-destroy'),

]
