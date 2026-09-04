from django.db import models

class HousePrediction(models.Model):
    location = models.CharField(max_length=100)
    sqft = models.IntegerField()
    bhk = models.IntegerField()
    bath = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return self.location
