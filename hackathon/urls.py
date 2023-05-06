from django.urls import path, include
from .views import (
    HackathonListCreateView,
    HackathonDetailView,
    registered_hackathons,
    register_for_hackathon,
)

urlpatterns = [
    path("", HackathonListCreateView.as_view(), name="hackathon-list"),
    path("<int:pk>/register/", register_for_hackathon, name="register-for-hackathon"),
    path("<int:pk>/", HackathonDetailView.as_view(), name="hackathon-detail"),
    path("registered/", registered_hackathons, name="registered-hackathons"),
]
