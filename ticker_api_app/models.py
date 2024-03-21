from django.db import models

# Create your models here.
class Ticker(models.Model):
    ticker=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    revenue=models.FloatField()
    gp=models.FloatField()
    fcf=models.FloatField(default=0)
    capex=models.FloatField(default=0)
