from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Expose the Post model in the Django admin for quick data entry."""

    list_display = ("title", "published_at")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "body")
    ordering = ("-published_at",)
