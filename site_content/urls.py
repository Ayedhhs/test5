from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home_view, signup_view

urlpatterns = [
    path('', home_view, name='home'),  # الصفحة الرئيسية
    path('signup/', signup_view, name='signup'),  # تسجيل الحساب
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),  # تسجيل الدخول
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),  # تسجيل الخروج (اختياري)
]
