from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from users.forms import RegisterForm, LoginForm
from django.contrib.auth import login, logout, authenticate


def register_view(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, "users/register.html", context={"form": form})
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.cleaned_data.__delitem__("password_confirm")
            user = User.objects.create_user(**form.cleaned_data)
            if user:
                return redirect("/")
                return HttpResponse(f"User created, {user.id}")
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