from django.urls import path
from .import views


app_name = 'Blog_Management_App'

urlpatterns = [
    path('', views.blogs, name='blogs'),
]
