"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from posts.views import test_view, homepage_view, posts_list_view ,post_detail_view, post_create_view
from users.views import register_view, login_view, logout_view
from django.conf.urls.static import static
from django.conf import settings

users_urls = [
    path('register/', register_view, name='register_view'),
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),
]

# старницы на сайте
urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test_view, name='test_view'),
    path('', homepage_view, name='html_view'),
    path('posts/', posts_list_view, name='posts_list_view'),  
    path('post/<int:post_id>/', post_detail_view, name="post_detail_view"),
    path('posts/create/', post_create_view, name='post_create_view'),
]
urlpatterns += users_urls + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)