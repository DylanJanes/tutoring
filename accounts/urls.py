from django.urls import path
from .views import SignUpView, add_availability, ProfileView, ReservationCreateView, ReservationDeleteView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("availability/", add_availability, name="add_availability"),
    path("reserve/", ReservationCreateView.as_view(), name="reserve_slot"),
    path("reservation/<int:pk>/delete/", ReservationDeleteView.as_view(), name="reservation_delete"),
    path("users/<int:pk>/", ProfileView.as_view(), name="user_detail"),
]
