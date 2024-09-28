from django.contrib import admin
from django.urls import path
from genres.views import GenreCreateListView, GenreRetrievelUpdateDestroyView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/', GenreCreateListView.as_view() , name='genre-create-list'),
    path('genres/<int:pk>', GenreRetrievelUpdateDestroyView.as_view(), name='genre-update-detail-destroy'),
]
