from django.contrib import admin
from .models import BlogPost, ContributorProfile, Certificate

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

@admin.register(ContributorProfile)
class ContributorProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "role",
        "created_at",
    )

    search_fields = (
        "user__username",
        "user__first_name",
        "user__last_name",
    )

    list_filter = (
        "role",
    )


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = (
        "certificate_id",
        "contributor",
        "role",
        "issue_date",
        "status",
    )

    list_filter = (
        "status",
        "role",
        "issue_date",
    )

    search_fields = (
        "certificate_id",
        "contributor__user__username",
        "contributor__user__first_name",
        "contributor__user__last_name",
        "contribution",
    )

    readonly_fields = (
        "certificate_id",
        "created_at",
    )