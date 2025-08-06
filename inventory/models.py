from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, default="")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)
    price = models.PositiveBigIntegerField() # Rupiah

    def __str__(self):
        return self.name


class StockMovement(models.Model):
    MOVEMENT_TYPE = (
        ('IN', 'In'),
        ('OUT', 'Out'),
    )
    type = models.CharField(max_length=3, choices=MOVEMENT_TYPE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} - {self.product.name}"
