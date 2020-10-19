from django.urls import path, include

from cart.views import CreateCartItem,ListCart,DetailCart,CreateCart,Updatecart,DeleteCart, ListCartItem,DetailCartItem, UpdateCartItem,DeleteCartItem

# Cart Urls
urlpatterns = [
    path('<int:pk>/cart/', ListCart, name='list-carts'),
    path('cart/<int:pk>/', DetailCart.as_view(), name='detail-cart'),
    path('cart/create/', CreateCart.as_view(), name='create-cart'),
    path('cart/<int:pk>/update/', Updatecart.as_view(), name='update-cart'),
    path('cart/<int:pk>/delete/', DeleteCart.as_view(), name='delete-cart'),
]

# CartItem Urls
urlpatterns += [
    path('cartitem/', ListCartItem.as_view(), name='list-cartitem'),
    path('cartitem/<int:pk>/', DetailCartItem.as_view(), name='detail-cartitem'),
    path('cartitem/create/', CreateCartItem.as_view(), name='create-cartitem'),
    path('cartitem/<int:pk>/update/', UpdateCartItem.as_view(), name='update-cartitem'),
    path('cartitem/<int:pk>/delete/', DeleteCartItem.as_view(), name='delete-cartitem'),
]