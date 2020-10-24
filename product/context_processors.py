def cartCount(request):
    from product.models import OrderItem
    return {'cartCount': OrderItem.objects.all()}
