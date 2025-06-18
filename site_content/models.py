from django.db import models

class AboutPage(models.Model):
    title = models.CharField(max_length=200, verbose_name="العنوان")
    content = models.TextField(verbose_name="المحتوى")

    def __str__(self):
        return self.title

class ContactInfo(models.Model):
    phone_number = models.CharField(max_length=20, verbose_name="رقم الجوال")
    email = models.EmailField(verbose_name="البريد الإلكتروني")
    address = models.TextField(blank=True, null=True, verbose_name="العنوان")

    def __str__(self):
        return self.phone_number
