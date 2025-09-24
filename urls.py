from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('desk_blog_project/urls.py', include('blog.urls')),
]
