from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import BlogPost


class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = "weekly"

    def items(self):
        return [
            "home",
            "documentation",
            "templates",
            "how_it_works",
            "research",
            "contribute",
            "blog",
            "roadmap",
            "about",
        ]

    def location(self, item):
        return reverse(item)


class BlogPostSitemap(Sitemap):
    priority = 0.7
    changefreq = "weekly"

    def items(self):
        return BlogPost.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return reverse(
            "blog_detail",
            kwargs={"slug": obj.slug}
        )