from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog


def blogs(request):
    return render(request, 'Blog_Management/blogs.html')


# write blog or create blog 
class WriteBlog(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'Blog_Management/write_blog.html'
    fields = ('blog_title', 'blog_content', 'blog_image', )

