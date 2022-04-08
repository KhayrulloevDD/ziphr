from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/zip_airlines/', include('zip_airlines.urls')),
]
