# task_manager/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # اضافه کن این خط
    path('', include('tasks.urls')),  # یا هر اسمی که برای urls برنامه‌ات داری
]