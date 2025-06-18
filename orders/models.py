from django.db import models
from products.models import Product

class Order(models.Model):
    customer_name = models.CharField(max_length=100, verbose_name="اسم العميل")
    customer_email = models.EmailField(verbose_name="البريد الإلكتروني")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"طلب رقم {self.id} - {self.customer_name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, verbose_name="الكمية")

    def __str__(self):
        return f"{self.quantity} × {self.product.name}"
