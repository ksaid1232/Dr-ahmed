from django.db import models


class ProductModel(models.Model):
    title = models.CharField(max_length=25)
    thumbnail = models.ImageField(upload_to="uploads/")
    short_description = models.CharField(max_length=100)
