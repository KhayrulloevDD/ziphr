import math

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator


class User(AbstractUser):

    def __str__(self):
        return self.username


class Airplane(models.Model):
    id = models.PositiveIntegerField('ID', primary_key=True, validators=[MinValueValidator(2)])
    passengers = models.PositiveIntegerField('Passengers', blank=True, null=True, validators=[MinValueValidator(0)])

    def capacity(self) -> int:
        return self.id * 200

    def consumption_per_minute(self) -> float:
        return round(math.log(self.id) * 0.8 + self.passengers * 0.002, 2)

    def able_to_fly(self) -> float:
        return round(self.capacity() / self.consumption_per_minute(), 2)

    def __str__(self):
        return str(self.id)
