from django.db import models

# Create your models here.

class Trip(models.Model):

    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=20)
    

    def __str__(self):
        return (self.city)