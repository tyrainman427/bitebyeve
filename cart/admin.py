from django.contrib import admin
from cart.models import Cart
from product.models import Product

# Register your models here.


class CartAdmin(admin.ModelAdmin):
    pass

class CartItemAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product)
admin.site.register(Cart)
