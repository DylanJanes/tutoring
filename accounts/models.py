from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.utils.timezone import now

# Create your models here.


class CustomUser(AbstractUser):
    displayName = models.CharField(default="Your Name",max_length=100)
    tutorFor = models.TextField(default="WRIT101")


class Availability(models.Model):
    DAYS_OF_WEEK = [
        (0, "Monday"),
        (1, "Tuesday"),
        (2, "Wednesday"),
        (3, "Thursday"),
        (4, "Friday"),
        (5, "Saturday"),
        (6, "Sunday"),
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
