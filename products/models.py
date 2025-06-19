from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم التصنيف")

    class Meta:
        verbose_name = "تصنيف"
        verbose_name_plural = "التصنيفات"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="اسم المنتج")
    description = models.TextField(verbose_name="الوصف")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="التصنيف")
    image = models.ImageField(upload_to='products/', null=True, blank=True, verbose_name="صورة المنتج")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="آخر تحديث")

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"

    def __str__(self):
        return self.name
