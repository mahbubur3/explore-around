from django.shortcuts import render


def blogs(request):
    return render(request, 'Blog_Management/blogs.html')
