from django.urls import path
from .views import SignUpView,add_availability, ProfileView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("availability/", add_availability, name="add_availability"),
    path("users/<int:pk>/", ProfileView.as_view(), name="user_detail"),
]
