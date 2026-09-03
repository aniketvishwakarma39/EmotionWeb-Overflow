from django.contrib import admin
from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "author",
        "is_featured",
        "is_published",
        "published_at",
    )

    list_filter = (
        "category",
        "is_published",
        "is_featured",
    )

    search_fields = (
        "title",
        "excerpt",
        "content",
        "tags",
        "author",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    list_editable = (
        "is_featured",
        "is_published",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
        "published_at",
    )

    fieldsets = (
        (
            "Article",
            {
                "fields": (
                    "title",
                    "slug",
                    "excerpt",
                    "cover_image",
                    "content",
                )
            },
        ),
        (
            "Classification",
            {
                "fields": (
                    "category",
                    "tags",
                    "author",
                )
            },
        ),
        (
            "SEO",
            {
                "fields": (
                    "seo_title",
                    "seo_description",
                ),
                "classes": ("collapse",),
            },
        ),
        (
            "Publishing",
            {
                "fields": (
                    "is_published",
                    "is_featured",
                    "published_at",
                )
            },
        ),
        (
            "Timestamps",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                ),
                "classes": ("collapse",),
            },
        ),
    )