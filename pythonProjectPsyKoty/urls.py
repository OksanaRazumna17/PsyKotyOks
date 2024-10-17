# pythonProjectPsyKoty/urls.py
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin_tools/', include('admin_tools.urls')),  # Додаємо URL для django-admin-tools
    path('admin/', admin.site.urls),  # URL для стандартної адмін-панелі
    path('', include('user_statistics.urls')),  # Головна сторінка через user_statistics
]





