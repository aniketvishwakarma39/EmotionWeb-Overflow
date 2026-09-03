from django.db import models
from django.utils import timezone


class BlogPost(models.Model):
    CATEGORY_CHOICES = [
        ("development", "Development"),
        ("research", "Research"),
        ("release", "Release"),
        ("tutorial", "Tutorial"),
        ("community", "Community"),
        ("other", "Other"),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)

    excerpt = models.TextField(max_length=400)

    cover_image = models.ImageField(
        upload_to="blog/covers/",
        blank=True,
        null=True
    )

    content = models.TextField()

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
        default="development"
    )

    tags = models.CharField(
        max_length=300,
        blank=True,
        help_text="Separate tags with commas."
    )

    author = models.CharField(
        max_length=100,
        default="EmotionWeb Team"
    )

    seo_title = models.CharField(
        max_length=200,
        blank=True
    )

    seo_description = models.CharField(
        max_length=300,
        blank=True
    )

    is_published = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(
        blank=True,
        null=True
    )

    class Meta:
        ordering = ["-published_at", "-created_at"]

    def save(self, *args, **kwargs):
        if self.is_published and self.published_at is None:
            self.published_at = timezone.now()

        if not self.is_published:
            self.published_at = None

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title