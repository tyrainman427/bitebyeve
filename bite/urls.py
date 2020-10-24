
from django.contrib import admin
from django.urls import path, include
from  django.conf.urls.static import static
from  django.conf import settings

urlpatterns = [
    path('', include('product.urls')),
    path('cart/',include('cart.urls')),
    path('admin/', admin.site.urls),
    path('s3direct/', include('s3direct.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
