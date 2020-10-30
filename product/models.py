from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime

DELIVERY = (
    ('Pick Up','Pick Up'),
    ('Delivery','Delivery'),
)

MENU = (
    ('Meal 1','Meal 1'),
    ('Meal 2','Meal 2'),
    ('Meal 3','Meal 3'),
    ('Meal 4','Meal 4'),
    ('VEGETARIAN OPTION','VEGETARIAN OPTION'),
)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("profile_detail", kwargs={"pk": self.pk})

class Product(models.Model):
    """ This the default Product class """
    name = models.CharField(max_length=50,choices=MENU, blank=True, null=True)
    description = models.TextField(max_length=100)
    photo = models.FileField()
    price = models.FloatField()
    delivery = models.CharField(max_length=10,default='Delivery',choices=DELIVERY)
    created_at = models.DateTimeField(default=datetime.now)
    add_on = models.CharField(max_length=200, blank=True, null=True)
    addOn_details = models.CharField(max_length=200, blank=True, null=True)

    ADDON_AMOUNT = 2.00

    def price_ttc(self):
        return self.price + self.ADDON_AMOUNT

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
    	try:
    	    url = self.photo.url
    	except:
    		url = ''
    	return url

    def get_absolute_url(self):
        return reverse("products:product_detail", kwargs={"pk": self.pk})

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True,blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_subtotal(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_item(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        full_total = total + 5
        return full_total

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True,blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True,blank=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True,blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True,blank=True)
    address = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=200,null=True)
    state = models.CharField(max_length=100,null=True)
    zipcode = models.CharField(max_length=200,null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
