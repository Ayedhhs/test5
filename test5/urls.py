from django.contrib import admin
from django.urls import path, include
from site_content.views import home_view  # ← استدعاء الصفحة الرئيسية

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', home_view, name='home'),  # ← هذا السطر الجديد لتوجيه /
    
    path('products/', include('products.urls')),
    path('orders/', include('orders.urls')),
    path('content/', include('site_content.urls')),
]
