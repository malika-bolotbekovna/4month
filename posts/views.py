from django.shortcuts import render, HttpResponse
import random
from posts.models import Post
from django.db.models import Q
from posts.forms import PostForm2, SearchForm
from django.contrib.auth.decorators import login_required



"""
posts = [post1, post2, post3, post4, post5, ..., post20]
limit = 4 (quantity of posts in 1 page)
page = 14

start = (page - 1) * limit
end = page * limit
"""

def test_view(request):
    return HttpResponse(f'hello, this is a test view, {random.randint(1, 100)}')

def homepage_view(request):
    if request.method == "GET":
        return render(request, 'base.html')

@login_required(login_url="login_view")
def posts_list_view(request):
    form = SearchForm()
    posts = Post.objects.all()
    limit = 4
    if request.method == "GET":
        query_params = request.GET
        search = query_params.get("search")
        category_id = query_params.get("category_id")
        tags = query_params.get("tags")
        ordering = query_params.get("ordering")
        page = query_params.get("page")
        page = int(page) if page else 1
        print(page)
        if search:
            posts = posts.filter(Q(title__icontains= search) | Q(content__icontains= search))
        if category_id:
            posts = posts.filter(category_id=int(category_id))   
        if tags:
            posts = posts.filter(tags__in=[int(tags) for tags in tags]).distinct() 
        if ordering:
            posts = posts.order_by(ordering)

        if page:
            max_pages = posts.count() / limit
            # max_pages = 20 / 4 = 5

            # max_pages = 13 / 4 = 3.25 -> 3(with(round))
            if round(max_pages) < max_pages:
                max_pages = round(max_pages) + 1
            # max_pages = 15 / 4 = 3.75 -> 4(with round())
            else:
                max_pages = round(max_pages)
            if int(page) > max_pages:
                page = max_pages
            start = (page - 1) * limit
            end = page * limit
            posts = posts[start:end]
        return render(request, "posts/posts_list.html", context={"posts": posts, "form": form, "max_pages": range(1, max_pages + 1)})



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
    