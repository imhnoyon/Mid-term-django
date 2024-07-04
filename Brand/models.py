from django.db import models
from django.utils.text import slugify
# Create your models here.
class Brands(models.Model):
    Brand_name=models.CharField(max_length=50)
    slug=models.SlugField(max_length=100,unique=True,null=True,blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.Brand_name)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.Brand_name