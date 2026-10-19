from django.urls import path
from .views import (
    SignUpView,
    ProfileView,
    AddAvailabilityView,
    EditAvailabilityView,
    DeleteAvailabilityView,
)

urlpatterns = [
    # User registration and profile
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/<int:pk>/", ProfileView.as_view(), name="user_detail"),
    # User availability
    path("availability/", AddAvailabilityView.as_view(), name="add_availability"),
    path(
        "availability/<int:pk>/edit/",
        EditAvailabilityView.as_view(),
        name="edit_availability",
    ),
    path(
        "availability/<int:pk>/delete/",
        DeleteAvailabilityView.as_view(),
        name="delete_availability",
    ),
]
