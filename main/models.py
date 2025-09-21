import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # tambahkan ini

    # Ngikut yg dari tutorial 0 aja
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)

    stock = models.PositiveIntegerField(default=0)
    product_views = models.PositiveIntegerField(default=0)


    # ngembaliin nama productnya
    def __str__(self):
        return self.name
    
    @property
    def is_product_hot(self):
        return self.product_views > 20
        
    def increment_views(self):
        self.product_views += 1
        self.save()
