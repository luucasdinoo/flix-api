from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/v1/', include('app_genres.urls')),
    path('api/v1/', include('app_actors.urls')),
    path('api/v1/', include('app_movies.urls')),
    path('api/v1/', include('app_reviews.urls')),    
    
]
