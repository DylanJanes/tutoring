from django.shortcuts import render, redirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, AvailabilityForm
from .models import Reservation

User = get_user_model()

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"

    def get_success_url(self):
        return reverse("user_detail",kwargs={"pk": self.object.pk})


@login_required
def add_availability(request):
    if request.method == "POST":
        form = AvailabilityForm(request.POST)

        if form.is_valid():
            availability = form.save(commit=False)
            availability.user = request.user
            availability.save()
            return redirect("add_availability")
    else:
        form = AvailabilityForm()

    availabilities = request.user.availabilities.all()

    return render(
        request,
        "accounts/availability_form.html",
        {
            "form": form,
            "availabilities": availabilities,
        },
    )

class ProfileView(DetailView):
    model = User
    template_name = "profile.html"
    context_object_name = "profile_user"


class ReservationCreateView(CreateView):
    model = Reservation
    template_name = "reserve_slot.html"
    fields = ["tutor", "day", "start_time", "end_time"]
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.student = self.request.user
        return super().form_valid(form)


class ReservationDeleteView(DeleteView):
    model = Reservation
    template_name = "reservation_confirm_delete.html"
    success_url = reverse_lazy("home")