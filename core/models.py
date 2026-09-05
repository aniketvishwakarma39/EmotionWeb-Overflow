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

import uuid

from django.conf import settings
from django.db import models


class ContributorProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="contributor_profile",
    )

    role = models.CharField(
        max_length=100,
        default="Contributor",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.user.get_full_name() or self.user.username
    
class Certificate(models.Model):
    STATUS_CHOICES = [
        ("issued", "Issued"),
        ("revoked", "Revoked"),
    ]

    certificate_id = models.CharField(
        max_length=50,
        unique=True,
        editable=False,
    )

    contributor = models.ForeignKey(
        ContributorProfile,
        on_delete=models.CASCADE,
        related_name="certificates",
    )

    contribution = models.TextField()

    role = models.CharField(
        max_length=100,
        default="Contributor",
    )

    issue_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="issued",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def save(self, *args, **kwargs):
        if not self.certificate_id:
            self.certificate_id = (
                f"EW-{self.issue_date.year}-"
                f"{uuid.uuid4().hex[:8].upper()}"
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return self.certificate_id