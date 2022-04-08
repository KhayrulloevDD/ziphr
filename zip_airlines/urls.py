from django.urls import path, include
from zip_airlines import apis

urlpatterns = [
    path('airplanes/', apis.AirplaneList.as_view()),
    path('airplanes/<int:pk>/', apis.AirplaneDetail.as_view()),
]
