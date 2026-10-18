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
        fields=("day","start_time","end_time",)
