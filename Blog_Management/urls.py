from django.urls import path
from .import views


app_name = 'Blog_Management_App'

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('write/', views.WriteBlog.as_view(), name='write_blog'),
]
