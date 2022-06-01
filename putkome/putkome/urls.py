
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('login.urls')),
    path('', include('tvseries.urls')),
    path('rating/', include('ratingapp.urls')),
]
