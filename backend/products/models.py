from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.TextField(blank=True, null=True, default=99.99)


    @property
    def sale_price(self):
        return '{:.2f}'.format(float(self.price) * 0.8)
    
    def get_discount(self):
        return '122'