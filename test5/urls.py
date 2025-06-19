from django.contrib import admin
from django.urls import path, include
from site_content.views import home_view  # استدعاء الصفحة الرئيسية

urlpatterns = [
    path('admin/', admin.site.urls),              # لوحة الإدارة
    path('', home_view, name='home'),             # الصفحة الرئيسية
    path('products/', include('products.urls')),  # روابط المنتجات
    path('orders/', include('orders.urls')),      # روابط الطلبات
    path('content/', include('site_content.urls'))  # محتوى الموقع
]
