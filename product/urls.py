from django.urls import path, include

from . import views

app_name = 'products'
# Product Urls
urlpatterns = [
    path('', views.index, name='product-list'),
    # path('product/', views.ProductListView.as_view(), name='product-list'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', views.ProductCreateView.as_view(), name='product-create'),
    path('product/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product-update'),
    path('product/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product-delete'),
    path('customer/<str:pk>/', views.customer_view, name='customer-detail'),
]

# Customer Urls
urlpatterns += [
    path('profiles/', views.CustomerListView.as_view(), name='profile-list'),
    path('profile/create/', views.CustomerCreateView.as_view(), name='profile-create'),
    path('profile/<int:pk>/update/', views.CustomerUpdateView.as_view(), name='profile-update'),
    path('profile/<int:pk>/delete/', views.CustomerDeleteView.as_view(), name='profile-delete'),
]
