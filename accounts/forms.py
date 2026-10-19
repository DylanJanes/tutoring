from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Availability

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "displayName",
            "tutorFor",
        )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "displayName",
            "tutorFor",
        )
    

class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = Availability
        fields = ("day", "start_time", "end_time")
        labels = {
            "day": "Day of the week",
            "start_time": "Start time",
            "end_time": "End time",
        }
        widgets = {
            "day": forms.Select(),
            "start_time": forms.TimeInput(
                format="%H:%M",
                attrs={"type": "time","step":"60"}
            ),
            "end_time": forms.TimeInput(
                format="%H:%M",
                attrs={"type": "time","step":"60"}
            ),
        }
