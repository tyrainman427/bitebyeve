from django.contrib import admin
from product.models import Product, Customer, Order, OrderItem, ShippingAddress

# @admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Product)
