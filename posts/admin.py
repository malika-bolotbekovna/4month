from django.contrib import admin
from posts.models import Post, Category, Tag

from posts.models import Post, Tag, Category

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "rate", "created_at", "updated_at", "author", "category")
    list_filter = ("rate", "category")
    search_fields = ("title", "content")
    # list_editable = ("author", "category",)


admin.site.register(Tag)
admin.site.register(Category)


