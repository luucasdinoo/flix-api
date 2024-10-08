from django.urls import path
from . import views


urlpatterns = [
    path('genres/', views.GenreCreateListView.as_view() , name='genre-create-list'),
    path('genres/<int:pk>', views.GenreRetrievelUpdateDestroyView.as_view(),       name='genre-update-detail-destroy'),
]
