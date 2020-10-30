from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from product.models import *
from product.utils import cookieCart, cartData, guestOrder
from django.http import JsonResponse
import json


def cart(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, "cart/cart.html",context)

def checkout(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, "cart/checkout.html",context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        # orderItem.quantity = (orderItem.quantity + 1)
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

        orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
		)

	return JsonResponse('Payment submitted..', safe=False)

##-------------- Cart Views --------------------------------------
# class DetailCart(DetailView):
#     model = Cart
#     template_name='cart/detail_cart.html'
#
# class ListCart(ListView):
#     model = Cart
#     context_object_name = 'carts'
#     template_name='cart/list_carts.html'
#
# class CreateCart(CreateView):
#     model = Cart
#     template_name = 'cart/create_cart.html'
#
# class Updatecart(UpdateView):
#     model = Cart
#     template_name = 'cart/update_cart.html'
#
# class DeleteCart(DeleteView):
#     model = Cart
#     template_name = 'cart/delete_cart.html'


##-------------- CartItem Views --------------------------------------
# class DetailCartItem(DetailView):
#     model = CartItem
#     template_name='cartitem/detail_cartitem.html'
#
# class ListCartItem(ListView):
#     model = CartItem
#     context_object_name = 'cartitems'
#     template_name='cartitem/list_cartitems.html'
#
# class CreateCartItem(CreateView):
#     model = CartItem
#     template_name = 'cartitem/create_cartitem.html'
#
# class UpdateCartItem(UpdateView):
#     model = CartItem
#     template_name = 'cartitem/update_cartitem.html'
#
# class DeleteCartItem(DeleteView):
#     model = Cart
#     template_name = 'cartitem/delete_cartitem.html'
