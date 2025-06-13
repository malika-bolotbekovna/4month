from django.db import models


# CharField() - as VARCHAR()
# auto_now_add - every time when added new
# auto_now - every time when changes
#  null true -
# blank true - 
# django orm


# команды sql в джанго:
# select * from posts -> Post.object.all()
# select * from posts where title Ilike '%test%' -> Post.objects.filter(title__icontains='test')
# select * frm posts is = 1 -> Post.objects.get(id=1)


# IN TERMINAL WE ALSO CAN GET DB OBJECTS:

# python manage.py shell

# >>> from posts.models import Post
# >>> 
# >>> posts = Post.objects.all()
# >>> print(posts)
# OUTPUT:
# <QuerySet [<Post: title1>, <Post: title2>, <Post: post without content>, <Post: good post>, <Post: post we need to find>]>

# >>> for post in posts:
# ...     print(post.title)
# ... 
# title1
# title2
# post without content
# good post
# post we need to find
# >>> for post in posts:
# ...     print(post.content)
# ... 
# desctiption1
# description2
# None
# smth
# content1

class Post(models.Model):
    title = models.CharField(max_length=256)
    content = models.CharField(max_length=512, null=True, blank=True)
    rate = models.CharField(default=0, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title