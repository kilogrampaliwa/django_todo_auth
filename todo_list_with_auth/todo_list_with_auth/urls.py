from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('accounts.urls')),
    path('admin/', admin.site.urls),

    path('tasks/', include('tasks.urls')),
    path('accounts/', include('accounts.urls')),
]
