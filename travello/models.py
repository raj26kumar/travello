from django.db import models

# Create your models here.

class Destination(models.Model):
    name = models.CharField(max_length=100)
    price =models.FloatField()
    img = models.ImageField(upload_to='images')
    desc = models.TextField()
    offer = models.BooleanField(default=False)
