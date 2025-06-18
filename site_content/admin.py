from django.contrib import admin
from .models import AboutPage, ContactInfo

@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title', 'content']

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone_number', 'email']
