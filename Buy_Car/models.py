from django.db import models
from django.contrib.auth.models import User
from Car.models import Car
# Create your models here.

class Purchase(models.Model):
     user = models.ForeignKey(User, related_name='purchases', on_delete=models.CASCADE)
     car = models.ForeignKey(Car, related_name='purchases1', on_delete=models.CASCADE)
     


     def __str__(self):
        return f'{self.user.username} bought {self.car.name}'