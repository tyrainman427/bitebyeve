from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.conf import settings
from datetime import datetime

User = get_user_model()

# DELIVERY = (
#     (False,'Pick Up'),
#     (True,'Delivery'),
# )

MENU = (
    ('Meal 1','Meal 1'),
    ('Meal 2','Meal 2'),
    ('Meal 3','Meal 3'),
    ('Meal 4','Meal 4'),
    ('VEGETARIAN OPTION','VEGETARIAN OPTION'),
    ('Sauce','Sauce')
)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("customer-details", kwargs={"pk": self.pk})

def post_save_customer_create(sender,instance,created,*args, **kwargs):
    if created:
        Customer.objects.get_or_create(user=instance)

post_save.connect(post_save_customer_create,sender=settings.AUTH_USER_MODEL)

class Product(models.Model):
    CATEGORY = (
        ('Meal','Meal'),('Vegetarian','Vegetarian'),('Sauces','Sauces'),
    )
    name = models.CharField(max_length=50,choices=MENU, blank=True, null=True)
    category = models.CharField(max_length=50,choices=CATEGORY, blank=True, null=True)
    description = models.TextField(max_length=100)
    photo = models.FileField()
    price = models.DecimalField(max_digits=5,decimal_places=2)
    created_at = models.DateTimeField(default=datetime.now)
    add_on = models.BooleanField(default=False)
    add_details = models.CharField(max_length=200, blank=True, null=True)

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
    STATUS = (
        ('Created','Created'),('Pending','Pending'),('Out For Delivery','Out For Delivery'),
        ('Ready For Pick Up','Ready For Pick Up')
    )
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True,blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    shipping = models.BooleanField(default=False)  #CharField(max_length=50,choices=DELIVERY, blank=True, null=True)
    complete = models.BooleanField(default=False)
    status = models.CharField(max_length=20,default="Created",choices=STATUS)
    transaction_id = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return str(self.id)

    # @property
    # def shipping(self):
    #     shipping = False
    #     orderitems = self.orderitem_set.all()
    #     for i in order.shipping:
    #         print(i)
    #         pickup = True
    #         return pickup

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_item(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

    @property
    def get_cart_subtotal(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        full_total = total + 5
        return full_total

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True,blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True,blank=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product)

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
