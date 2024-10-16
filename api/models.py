from django.db import models

# Create your models here.

class Location(models.Model):
    location_name = models.CharField(max_length=100, unique=True)
    
    def __str__(self) -> str:
        return self.location_name

class Items(models.Model):
    item_name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    item_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.item_name