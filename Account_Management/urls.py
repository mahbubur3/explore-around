from django.urls import path
from .import views


app_name = 'Account_Management_App'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
]
