from django.db import models
from Brand.models import Brands
# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Car/media/uploades/', blank=True, null=True)

    def __str__(self):
        return self.name
    

class Comment(models.Model):
    post=models.ForeignKey(Car,on_delete=models.CASCADE, related_name='comments')
    name=models.CharField(max_length=30)
    email=models.EmailField()
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comments by {self.name}'