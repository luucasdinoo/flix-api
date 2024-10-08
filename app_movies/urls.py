from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.MovieCreateListView.as_view(), name= 'movie-create-list'),
    path('movies/<int:pk>/', views.MovieRetrievelUpdateDestroyView.as_view(), 
    name= 'movie-update-detail-destroy'),
]
