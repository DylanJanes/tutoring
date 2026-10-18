from django.urls import path
from .views import SignUpView,add_availability

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("availability/", add_availability, name="add_availability"),
]
