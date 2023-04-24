from django.db import models

# Create your models here.


class Customer(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=80, unique=True)
    password = models.CharField(max_length=80, null=False)

    def __str__(self) -> str:
        return self.username
