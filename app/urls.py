from django.urls import path
from app import views

urlpatterns = [
    path("profile", views.profile),
    path("history", views.history),
]