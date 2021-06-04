
from django.contrib import admin
from django.urls import path, include 
from task_list import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('task_list.urls')),
]
