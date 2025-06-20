from django.shortcuts import render, HttpResponse
import random
from posts.models import Post
from posts.forms import PostForm, PostForm2
from django.contrib.auth.decorators import login_required

def test_view(request):
    return HttpResponse(f'hello, this is a test view, {random.randint(1, 100)}')

def homepage_view(request):
    if request.method == "GET":
        return render(request, 'base.html')

@login_required(login_url="login_view")
def posts_list_view(request):
    if request.method == "GET":
        posts = Post.objects.all()
        return render(request, "posts/posts_list.html", context={"posts": posts})

@login_required(login_url="login_view")
def post_detail_view(request, post_id):
    if request.method == "GET":
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return HttpResponse("Post not found")
        
        return render(request, "posts/post_detail.html", context={"post": post})
    
@login_required(login_url="login_view")
def post_create_view(request):
    if request.method == "GET":
        form = PostForm2()
        return render(request, "posts/post_create.html", context={"form": form})
    if request.method == "POST":
        form = PostForm2(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            content = form.cleaned_data.get("content")
            image = form.cleaned_data.get("image")
            Post.objects.create(image = image, title=title, content = content)
            return HttpResponse("post created")
        else:
            return render(request, "posts/post_create.html", context={"form": form})
    