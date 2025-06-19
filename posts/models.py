# создает таблицы бд с помощью python-классов 
from django.db import models


"""CharField() - as VARCHAR()
auto_now_add - every time when added new
auto_now - every time when changes
 null true -поле в бд может быть пустым
blank true - в форме(на сайте может быть пустым)
null=True, blank=True — поле можно не заполнять ни в форме, ни в базе (будет NULL)
null=False, blank=True — форма разрешает оставить пустым, но в БД сохранится '' (пустая строка)

objects - для выполнения запросов к бд
 filter(...) - набор записей подходящие под условие внутри скобок

title__icontains='test':
title - поле по которому ищем
contains - ищем подстроку
icontains - ищем под строку без учета регистра"""



# команды sql в джанго:
"""select * from posts -> Post.object.all()
select * from posts where title Ilike '%test%' -> Post.objects.filter(title__icontains='test')
select * frm posts is = 1 -> Post.objects.get(id=1)
insert into posts(title, content) values('fgdfdddd', 'vbdgddd') ->
 Post.objects.create(title='fgdfdddd', content='vbdgddd')"""


# IN TERMINAL WE ALSO CAN GET DB OBJECTS:
"""python manage.py shell

импорт таблицы
>>> from posts.models import Post
>>> 
команда чтобы выбрать все из таблицы
>>> posts = Post.objects.all()
>>> print(posts)
OUTPUT:
выводит список загаловок, потому что класс пост возвращает загаловок(метод есть)
<QuerySet [<Post: title1>, <Post: title2>, <Post: post without content>, <Post: good post>, <Post: post we need to find>]>

>>> for post in posts:
...     print(post.title)
... 
title1
title2
post without content
good post
post we need to find
>>> for post in posts:
...     print(post.content)
... 
desctiption1
description2
None
smth
content1"""



class Category(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name
    

class Tag(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

# django orm
class Post(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=256)
    content = models.CharField(max_length=512, null=True, blank=True)
    rate = models.CharField(default=0, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True
    )
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title