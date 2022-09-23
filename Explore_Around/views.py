from django.urls import reverse
from django.shortcuts import HttpResponseRedirect


def index(request):
    
    return HttpResponseRedirect(reverse('Blog_Management_App:all_blog'))