from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    pass 

class Airport(models.Model):
    city = models.CharField(max_length=50)
    code = models.CharField(max_length=3)


    def __str__(self):
        return f"{self.code}"
    

class Flight(models.Model):
    origin =  models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departures')
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals')
    duration = models.IntegerField(default=200)

    def __str__(self):
        return f"{self.origin} ---> {self.destination})"
    

class Passenger(models.Model):
    first_name = models.CharField(null=False, blank=False, max_length=100)
    last_name = models.CharField(null=False, blank=False, max_length=100)
    flight = models.ManyToManyField(Flight, related_name='passengers')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
