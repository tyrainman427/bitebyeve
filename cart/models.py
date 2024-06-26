from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

from product.models import Product

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.FloatField(blank=True)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)

    TAX_AMOUNT = 6.35

    def price_ttc(self):
        return self.price * (1 + TAX_AMOUNT/100.0)

    def __str__(self):
        return  self.client + " - " + self.product
