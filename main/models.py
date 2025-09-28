from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('sepatu', 'Sepatu'),
        ('bola', 'Bola'),
        ('aksesoris', 'Aksesoris'),
        ('random', 'Random')
    ]

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    is_featured = models.BooleanField(default=False)

    # fitur tambahan
    stock = models.PositiveIntegerField(default=0)
    brand = models.CharField(max_length=50, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    # Menghubungkan User dengan product
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    persona = models.TextField()



