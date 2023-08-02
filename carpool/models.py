from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_driver = models.BooleanField(default=False)
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
    smoking = models.BooleanField(default=False)
    pets = models.BooleanField(default=False)
    chat = models.BooleanField(default=False)
    music = models.BooleanField(default=False)


class Car(models.Model):
    owner = models.ForeignKey(User, related_name="cars", on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    seats = models.IntegerField()
    smoking_allowed = models.BooleanField(default=False)
    pets_allowed = models.BooleanField(default=False)


class Trip(models.Model):
    driver = models.ForeignKey(
        User, related_name="driven_trips", on_delete=models.CASCADE
    )
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_location = models.CharField(max_length=200)
    end_location = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    max_divert_distance = models.FloatField(
        help_text="Maximum distance the driver is willing to divert from the route, in km"
    )


class TripHistory(models.Model):
    user = models.ForeignKey(
        User, related_name="trip_history", on_delete=models.CASCADE
    )
    trip = models.ForeignKey(
        Trip, related_name="trip_history", on_delete=models.CASCADE
    )
    price = models.FloatField(help_text="Price paid for the trip")
