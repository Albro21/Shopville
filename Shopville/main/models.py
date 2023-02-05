from django.db import models

# Create your models here.


class Goods(models.Model):
    item_name = models.CharField(max_length=50, default='Product name')
    item_description = models.TextField(max_length=1000, default='Product description')
    item_image = models.ImageField(upload_to='images')
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.01)
    sellers_email = models.EmailField(blank=True)

    def __str__(self):
        return self.item_name
