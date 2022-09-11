from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')
    blog_title = models.CharField(max_length=264, verbose_name='Title')
    slug = models.SlugField(max_length=264, unique=True)
    blog_content = models.TextField(verbose_name='Please wirte what is on your mind?')
    blog_image = models.ImageField(upload_to='blog_pics', verbose_name='Image')
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blog_title