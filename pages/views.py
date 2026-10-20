from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
from django.urls import reverse
from accounts.models import Availability
import json

User = get_user_model()

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #events stores stuff in dictionary format (eventually read as a json) as such
        #title: "Bob - CS 101",
        #daysOfWeek: [1],
        #startTime: "09:00:00",
        #endTime: "11:00:00",
        #url: "/accounts/users/5/"
        events = []

        availabilities = Availability.objects.select_related("user").all()

        for availability in availabilities:
            events.append({
                "title": (
                    f"{availability.user.displayName} - "
                    f"{availability.user.tutorFor}"
                ),

                "daysOfWeek": [availability.day],

                "startTime": availability.start_time.strftime("%H:%M:%S"),
                "endTime": availability.end_time.strftime("%H:%M:%S"),

                "url": reverse("user_detail",kwargs={"pk": availability.user.pk}),
            })

        context["calendar_events"] = json.dumps(events)

        context["users"] = User.objects.all()

        return context
