from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.timezone import now

# Create your models here.


class CustomUser(AbstractUser):
    displayName = models.CharField(default="Your Name",max_length=100)
    tutorFor = models.TextField(default="WRIT101")


class Availability(models.Model):
    DAYS_OF_WEEK = [ #This has to start at 1 instead of 0 for FullCalender, used in home.html
        (1, "Monday"),
        (2, "Tuesday"),
        (3, "Wednesday"),
        (4, "Thursday"),
        (5, "Friday"),
        (6, "Saturday"),
        (7, "Sunday"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="availabilities",
    )

    day = models.IntegerField(choices=DAYS_OF_WEEK)
    start_time = models.TimeField(default=now().time())
    end_time = models.TimeField(default=now().time())

    def __str__(self):
        return(f"{self.user} - {self.get_day_display()} " f"{self.start_time} to {self.end_time}")


class Reservation(models.Model):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="reservations",
        null=True, #Allows saving when not logged in.
        blank=True, #Allows form to submit when not logged in.
    )
    tutor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tutor_reservations",
    )
    day = models.CharField(
        max_length=15,
        choices=[
            ("Monday", "Monday"),
            ("Tuesday", "Tuesday"),
            ("Wednesday", "Wednesday"),
            ("Thursday", "Thursday"),
            ("Friday", "Friday"),
        ],
    )

    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return (f"{self.student.username} with {self.tutor.username} ({self.day} {self.start_time})")

    def get_absolute_url(self):
        return reverse("home")