from django.http import HttpResponse
from .models import Product

# عرض قائمة المنتجات بدون قالب HTML
def product_list_view(request):
    products = Product.objects.all()

    html = """
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <title>قائمة المنتجات</title>
        <style>
            body {
                font-family: Tahoma, sans-serif;
                background-color: #f9f9f9;
                padding: 40px;
                text-align: right;
            }
            h1 {
                color: #00aa66;
                margin-bottom: 30px;
            }
            .product {
                background-color: #fff;
                border: 1px solid #ddd;
                padding: 20px;
                margin-bottom: 15px;
                border-radius: 10px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }
            .product h3 {
                margin: 0 0 10px;
                color: #333;
            }
            .product p {
                margin: 5px 0;
                color: #555;
            }
        </style>
    </head>
    <body>
        <h1>المنتجات المتوفرة</h1>
    """

    if products:
        for product in products:
            html += f"""
            <div class="product">
                <h3>{product.name}</h3>
                <p>{product.description}</p>
                <p><strong>السعر:</strong> {product.price} ريال</p>
            </div>
            """
    else:
        html += "<p>لا توجد منتجات متاحة حالياً.</p>"

    html += "</body></html>"

    return HttpResponse(html)
