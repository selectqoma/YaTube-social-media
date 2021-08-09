from django.contrib import admin

from .models import Comment, Group, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("pk", "text", "pub_date", "author")
    search_fields = ("text",)
    list_filter = ("pub_date",)
    empty_value_display = "-empty-"


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "slug", "description")
    search_fields = ("description",)
    list_filter = ("title",)
    empty_value_display = "-empty-"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "text")
    search_fields = ("post",)
    list_filter = ("created",)
    empty_value_display = "-empty-"
