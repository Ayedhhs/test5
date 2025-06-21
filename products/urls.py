from django.urls import path
from . import views

# تعريف namespace الخاص بتطبيق المنتجات لتجنب تعارض الأسماء في reverse
app_name = 'products'

urlpatterns = [
    # عرض قائمة المنتجات
    path('', views.product_list_view, name='product_list'),
]
