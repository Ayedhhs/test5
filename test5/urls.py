from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # توجيه روابط التطبيقات الداخلية
    path('products/', include('products.urls')),
    path('orders/', include('orders.urls')),
    path('content/', include('site_content.urls')),
]
