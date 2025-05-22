# african_cities/models.py
from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField()

    def __str__(self):
        return f"{self.name} - {self.country}"
