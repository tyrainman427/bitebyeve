from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .utils import cookieCart, cartData, guestOrder
from .models import *


# Create your views here.
def index(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    products = Product.objects.all()
    context = {'products':products, 'cartItems':cartItems}

    return render(request,'product/product_list.html',context)

def customer_view(request, pk):
    customer = Customer.objects.filter(user=request.user).first()
    my_order = Order.objects.all()
    orders = Order.customer.filter(complete=True)
    order_count = my_order.count()
    context = {'customer':customer, 'orders':orders,'order_count':order_count}
    return render(request, 'product/customer.html',context)

# Product views
class ProductDetailView(DetailView):
    model = Product
    template_name = "product/product_detail.html"

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Product, id=id_)

# class ProductListView(ListView):
#     model = Product
#     queryset = Product.objects.all()
#     template_name = "product/product_list.html"

class ProductCreateView(CreateView):
    model = Product
    template_name = "product/product_create.html"
    fields = ['name','description','price','add_on','photo']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class ProductUpdateView(UpdateView):
    model = Product
    template_name = "product/product_update.html"

class ProductDeleteView(DeleteView):
    model = Product
    template_name = "product/product_delete.html"


# UserProfile views
# class CustomerDetailView(DetailView):
#     model = Customer
#     template_name = "product/customer.html"
#
#     def get_object(self):
#         id_ = self.kwargs.get("id")
#         return get_object_or_404(Customer, id=id_)

class CustomerListView(ListView):
    model = Customer
    template_name = "product/customer_list.html"

class CustomerCreateView(CreateView):
    model = Customer
    template_name = "product/userprofile_create.html"

class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = "product/userprofile_update.html"

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = "product/userprofile_delete.html"
