from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog
import uuid
from django.urls import reverse


def blogs(request):
    return render(request, 'Blog_Management/blogs.html')


# write blog or create blog 
class WriteBlog(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'Blog_Management/write_blog.html'
    fields = ('blog_title', 'blog_content', 'blog_image', )

    def form_valid(self, form):
        blog_obj = form.save(commit=False)
        blog_obj.author = self.request.user
        title = blog_obj.blog_title

        # add 4 unique id in url
        blog_obj.slug = title.replace(" ", "-") + "-" + str(uuid.uuid4())
        blog_obj.save()
        return HttpResponseRedirect(reverse('index'))

