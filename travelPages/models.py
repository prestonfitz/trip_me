from django.db import models

# Create your models here.

class tripInfo(models.Model):

    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30,null=True,blank=True)
    country = models.CharField(max_length=30)
    description = models.TextField(max_length=1000)
    length = models.IntegerField(default=0)
    cost = models.FloatField(default=0.00)
    picture = models.CharField(max_length=30)

    def __str__(self):
        return self.location
    
    def location(self):
        return '%s %s' (self.city, self.country)