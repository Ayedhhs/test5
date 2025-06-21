from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from products.models import Product

# عرض الصفحة الرئيسية مع المنتجات
def home_view(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


# عرض صفحة تسجيل حساب جديد
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'site_content/signup.html', {'form': form})


# عرض صفحة تسجيل الدخول باستخدام قالب مخصص
class CustomLoginView(LoginView):
    template_name = 'site_content/login.html'
