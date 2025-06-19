from django.contrib import admin
from django.urls import path, include
from site_content.views import home_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),              # لوحة التحكم
    path('', home_view, name='home'),             # الصفحة الرئيسية
    path('products/', include('products.urls')),  # روابط المنتجات
    path('orders/', include('orders.urls')),      # روابط الطلبات
    path('content/', include('site_content.urls'))  # محتوى الموقع
]

# عرض ملفات media (مثل صور المنتجات) في وضع التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
