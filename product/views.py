from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from .models import Product, Customer


# Create your views here.
def index(request):
    return render(request,'menu/index.html',{})

# Product views
class ProductDetailView(DetailView):
    model = Product
    template_name = "product/product_detail.html"

class ProductListView(ListView):
    model = Product
    template_name = "product/product_list.html"

class ProductCreateView(CreateView):
    model = Product
    template_name = "product/product_create.html"
    fields = ['name','description','price_ht','photo']

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
class CustomerDetailView(DetailView):
    model = Customer
    template_name = "product/userprofile_detail.html"

class CustomerListView(ListView):
    model = Customer
    template_name = "product/userprofile_list.html"

class CustomerCreateView(CreateView):
    model = Customer
    template_name = "product/userprofile_create.html"

class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = "product/userprofile_update.html"

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = "product/userprofile_delete.html"