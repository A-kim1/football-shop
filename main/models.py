import uuid
from django.db import models

class Product(models.Model):
    # Ngikut yg dari tutorial 0 aja
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)

    stock = models.PositiveIntegerField(default=0)


    # ngembaliin nama productnya
    def __str__(self):
        return self.name
