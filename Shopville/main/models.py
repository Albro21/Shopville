from django.db import models

# Create your models here.


class Goods(models.Model):
    item_name = models.CharField(max_length=50, default='No product name')
    item_description = models.TextField(max_length=1000, default='No product description')
    item_image = models.ImageField(upload_to='images')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    sellers_email = models.EmailField()

    def __str__(self):
        return self.item_name
