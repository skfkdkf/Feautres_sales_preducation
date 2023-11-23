from django.db import models

# Create your models here.
class Features_sales_preduction(models.Model):
    TV = models.CharField(max_length=255, blank=True, null=True)
    Radio = models.CharField(max_length=255, blank=True, null=True)
    Newspaper = models.CharField(max_length=255, blank=True, null=True)
    
    
class Predict(models.Model):
    Predict = models.CharField(max_length=255, blank=True, null=True)
