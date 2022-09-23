from django.urls import path
from .import views


app_name = 'Blog_Management_App'

urlpatterns = [
    path('', views.AllBlog.as_view(), name='all_blog'),
    path('write/', views.WriteBlog.as_view(), name='write_blog'),
    path('<str:slug>', views.full_blog, name='full_blog'),
]
