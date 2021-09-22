from django.db import models

class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=50)
    product_price = models.DecimalField(max_digits=10,decimal_places=2)
    product_color = models.CharField(max_length=20)

    def __str__(self):
        return self.product_name
