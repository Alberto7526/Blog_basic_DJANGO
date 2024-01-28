from django.contrib import admin
from apps.posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "user", "published", "created_at"]
