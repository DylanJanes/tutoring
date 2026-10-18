
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm, AvailabilityForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


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
