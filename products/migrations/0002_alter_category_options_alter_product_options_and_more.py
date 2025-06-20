# Generated by Django 5.2.3 on 2025-06-19 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'تصنيف', 'verbose_name_plural': 'التصنيفات'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'منتج', 'verbose_name_plural': 'المنتجات'},
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='صورة المنتج'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإضافة'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='آخر تحديث'),
        ),
    ]
