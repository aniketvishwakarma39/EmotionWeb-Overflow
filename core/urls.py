from django.contrib.sitemaps.views import sitemap
from django.urls import path

from . import views
from .sitemaps import StaticViewSitemap, BlogPostSitemap


urlpatterns = [
    path("", views.home, name="home"),

    path("docs/", views.documentation, name="documentation"),

    path("templates/", views.templates, name="templates"),

    path("how-it-works/", views.how_it_works, name="how_it_works"),

    path("research/", views.research, name="research"),

    path("contribute/", views.contribute, name="contribute"),

    path("blog/", views.blog, name="blog"),

    path(
        "blog/<slug:slug>/",
        views.blog_detail,
        name="blog_detail",
    ),

    path("roadmap/", views.roadmap, name="roadmap"),

    path("about/", views.about, name="about"),

    path(
        "robots.txt",
        views.robots_txt,
        name="robots_txt",
    ),

    path(
        "sitemap.xml",
        sitemap,
        {
            "sitemaps": {
                "static": StaticViewSitemap,
                "blog": BlogPostSitemap,
            }
        },
        name="sitemap",
    ),
]