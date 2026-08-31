from django.contrib import admin
from .models import Category, Blog


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "category_name", "created_at", "updated_at")
    search_fields = ("category_name",)
    ordering = ("id",)
    # filter_horizontal = ("category_name",)


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        "id",
        "title",
        "category",
        "status",
        "is_featured",
        "created_at",
    )
    search_fields = (
        "title",
        "category__category_name",
        "slug",
        "status",
        "author__username",
    )
    ordering = ("id",)
    list_editable = ("is_featured","status")


admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
