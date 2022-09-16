from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('Account_Management.urls')),
    path('blog/', include('Blog_Management.urls')),
    path('', views.index, name='index'),
]
