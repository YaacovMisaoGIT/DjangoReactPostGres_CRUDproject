from django.contrib import admin
from django.urls import path
from .views import PyAppView

urlpatterns = [
    path("PyApp/", PyAppView.as_view()),
    path("PyApp/<int:pk>/", PyAppView.as_view())
]