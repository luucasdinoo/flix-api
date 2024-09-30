from django.contrib import admin
from django.urls import path
from app_genres.views import GenreCreateListView, GenreRetrievelUpdateDestroyView
from app_actors.views import ActorCreateListView, ActorRetrieveUpdateDestroy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/', GenreCreateListView.as_view() , name='genre-create-list'),
    path('genres/<int:pk>', GenreRetrievelUpdateDestroyView.as_view(),                        name='genre-update-detail-destroy'),
    
    path('actors/', ActorCreateListView.as_view(), name= 'actor-create-list'),
    path('actors/<int:pk>/', ActorRetrieveUpdateDestroy.as_view(), 
    name= 'actor-update-detail-destroy'),
]
