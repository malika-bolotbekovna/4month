from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from users.models import Profile
from users.forms import RegisterForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required



def register_view(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, "users/register.html", context={"form": form})
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.cleaned_data.__delitem__("password_confirm")
            avatar = form.cleaned_data.pop("avatar", None)
            age = form.cleaned_data.pop("age", None)
            user = User.objects.create_user(**form.cleaned_data)
            if user:
                Profile.objects.create(user=user, avatar=avatar,age=age)
                return redirect("/")
            else:
                return HttpResponse("User not created")
        else:
            return render(request, "users/register.html", context={"form": form})
        

def login_view(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "users/login.html", context={"form": form})
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user:
                login(request, user)
                return redirect("/")
            else:
                form.add_error(None, "Invalid username or password")
                return render(request, "users/login.html", context={"form": form})
        else:
            return render(request, "users/register.html", context={"form": form})    
        

def logout_view(request):
    logout(request)
    return redirect("/")

@login_required(login_url="login_view")
def profile_view(request):
    user = request.user
    if user:
        profile =Profile.objects.get(user=user)
        user_posts = user.posts.all()
        return render(request, "users/profile.html", context={"profile": profile, "posts": user_posts})
    else:
        return HttpResponse("User not found")
