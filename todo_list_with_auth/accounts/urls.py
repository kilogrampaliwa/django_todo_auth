from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from .views import register

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),  # Includes default auth URLs
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('pending/', TemplateView.as_view(template_name='accounts/registration_pending.html'), name='registration-pending'),
]