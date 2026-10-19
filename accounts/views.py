from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model

from .forms import CustomUserCreationForm, AvailabilityForm
from .models import Availability

User = get_user_model()


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"

    def get_success_url(self):
        return reverse("user_detail", kwargs={"pk": self.object.pk})


class AddAvailabilityView(LoginRequiredMixin, CreateView):
    model = Availability
    form_class = AvailabilityForm
    template_name = "accounts/availability_form.html"
    success_url = reverse_lazy("add_availability")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["availabilities"] = (
            self.request.user.availabilities.all()
        )
        return context


class EditAvailabilityView(LoginRequiredMixin, UpdateView):
    model = Availability
    form_class = AvailabilityForm
    template_name = "accounts/edit_availability.html"
    success_url = reverse_lazy("add_availability")

    def get_queryset(self):
        return Availability.objects.filter(user=self.request.user)


class DeleteAvailabilityView(LoginRequiredMixin, DeleteView):
    model = Availability
    template_name = "accounts/delete_availability.html"
    success_url = reverse_lazy("add_availability")

    def get_queryset(self):
        return Availability.objects.filter(user=self.request.user)


class ProfileView(DetailView):
    model = User
    template_name = "profile.html"
    context_object_name = "profile_user"
