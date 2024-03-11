from django.shortcuts import render
from blog.models import Post


def index(request):
    return render(request, "main/index.html")


def blog_list(request):
    posts = Post.objects.all()
    return render(request, {"posts": posts})
