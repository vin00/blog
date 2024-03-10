from django.shortcuts import render
from .models import Post, Comment, Tag
from .forms import CommentForm


def blog_list(request):
    posts = Post.objects.all()
    return render(request, "blog/index.html", {"posts": posts})


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            author = request.user
            message = form.cleaned_data["message"]
            c = Comment.objects.create(author=author, message=message, post=post)
            c.save()
    if request.method == "GET":
        post.view_count += 1
        post.save()
    return render(
        request,
        "blog/blog_detail.html",
        {"post": post, "form": form},
    )


@login_required
def blog_create(request):
    if request.method == "GET":
        form = PostForm()
        context = {"form": form}
        return render(request, "blog/blog_detail.html", context)
    elif request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect("blog_list")
        else:
            context = {"form": form}
            return render(request, "blog/blog_create.html", context)


def blog_update(request, pk):
    pass


def blog_delete(request, pk):
    pass


def blog_tag(request, tag):
    posts = Post.objects.filter(tags__name__iexact=tag)
    # exact에 i가 붙으면 대소문자 구분하지 않음.
    return render(request, "blog/blog_list.html", {"posts": posts})
