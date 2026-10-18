from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
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
