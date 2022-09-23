from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog
import uuid
from django.urls import reverse
from .forms import CommentForm


def blogs(request):
    return render(request, 'Blog_Management/all_blog.html')


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


# all blog
class AllBlog(ListView):
    context_object_name = 'blogs'
    model = Blog
    template_name = 'Blog_Management/all_blog.html'


# show full blog 
def full_blog(request, slug):
    blog = Blog.objects.get(slug=slug)
    comment_form = CommentForm()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            return HttpResponseRedirect(reverse('Blog_Management_App:full_blog', kwargs={'slug':slug}))

    return render(request, 'Blog_Management/full_blog.html', {'blog': blog, 'comment_form': comment_form})