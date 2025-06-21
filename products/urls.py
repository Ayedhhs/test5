from django.urls import path
from . import views

app_name = 'products'  # تعريف namespace اللازم لتجنب خطأ NoReverseMatch

urlpatterns = [
    path('', views.product_list_view, name='product_list'),  # اسم العرض الرئيسي للمنتجات
]
