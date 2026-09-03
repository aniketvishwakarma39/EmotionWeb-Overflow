from django.urls import path

from . import views


urlpatterns = [

    path("", views.home, name="home"),

    path(
        "docs/",
        views.documentation,
        name="documentation"
    ),

    path(
        "templates/",
        views.templates,
        name="templates"
    ),

    path(
        "how-it-works/",
        views.how_it_works,
        name="how_it_works"
    ),

    path(
        "research/",
        views.research,
        name="research"
    ),

    path(
        "contribute/",
        views.contribute,
        name="contribute"
    ),

    path(
        "blog/",
        views.blog,
        name="blog"
    ),

    path(
        "about/",
        views.about,
        name="about"
    ),

]