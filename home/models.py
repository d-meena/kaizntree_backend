from django.db import models

# Create your models here.
class Tag(models.Model):
    name=models.CharField(max_length=30, primary_key=True)
    tag_image = models.ImageField(upload_to='static/images')

class Product(models.Model):
    SKU = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    instock = models.FloatField()
    available_stock = models.FloatField()
    tags = models.ManyToManyField(Tag, related_name='products', blank=True)



    