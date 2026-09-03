from django.core.cache import cache
from django.shortcuts import render

import json
from urllib.request import Request, urlopen


PYPI_URL = "https://pypi.org/pypi/emotionweb/json"
PYPI_STATS_URL = "https://pypistats.org/api/packages/emotionweb/overall"


def fetch_json(url):
    """
    Fetch JSON data from an external API.
    """

    request = Request(
        url,
        headers={
            "User-Agent": "EmotionWeb-Docs/1.0"
        }
    )

    with urlopen(
        request,
        timeout=8
    ) as response:

        return json.loads(
            response.read().decode("utf-8")
        )


def get_package_stats():
    """
    Get real EmotionWeb package information
    from PyPI and PyPI Stats.

    Cached for one hour so we don't request
    external APIs on every page load.
    """

    cached_data = cache.get(
        "emotionweb_package_stats"
    )

    if cached_data:
        return cached_data


    # ---------------------------------------------------------
    # Default fallback
    # ---------------------------------------------------------

    package_data = {
        "version": "0.2.3",
        "author": "Aniket Vishwakarma",
        "owner": "aniketvishwa39",
        "python": ">=3.10",
        "downloads": "Unavailable",
    }


    try:

        # -----------------------------------------------------
        # PYPI PROJECT DATA
        # -----------------------------------------------------

        pypi_data = fetch_json(
            PYPI_URL
        )

        info = pypi_data.get(
            "info",
            {}
        )


        # Version

        if info.get("version"):
            package_data["version"] = (
                info["version"]
            )


        # Author

        if info.get("author"):
            package_data["author"] = (
                info["author"]
            )


        # Python requirement

        if info.get("requires_python"):
            package_data["python"] = (
                info["requires_python"]
            )


        # -----------------------------------------------------
        # PYPI OWNER
        # -----------------------------------------------------

        ownership = pypi_data.get(
            "ownership",
            {}
        )

        roles = ownership.get(
            "roles",
            []
        )


        owners = [
            role
            for role in roles
            if role.get("role") == "Owner"
        ]


        if owners:

            package_data["owner"] = (
                owners[0].get(
                    "user",
                    "aniketvishwa39"
                )
            )


    except Exception as error:

        print(
            "PyPI package API error:",
            error
        )


    try:

        # -----------------------------------------------------
        # PYPI DOWNLOAD STATISTICS
        # -----------------------------------------------------

        stats_data = fetch_json(
            PYPI_STATS_URL
        )


        rows = stats_data.get(
            "data",
            []
        )


        # Only downloads without mirrors

        without_mirrors = [
            row
            for row in rows
            if row.get("category")
            == "without_mirrors"
        ]


        total_downloads = sum(
            int(
                row.get(
                    "downloads",
                    0
                )
                or 0
            )
            for row in without_mirrors
        )


        package_data["downloads"] = (
            total_downloads
        )


    except Exception as error:

        print(
            "PyPI Stats API error:",
            error
        )


    # ---------------------------------------------------------
    # CACHE
    # ---------------------------------------------------------

    cache.set(
        "emotionweb_package_stats",
        package_data,
        60 * 60
    )


    return package_data


def get_page_context():
    """
    Common context shared by all pages.
    """

    return {
        "package": get_package_stats()
    }


# =============================================================
# PAGES
# =============================================================

def home(request):

    return render(
        request,
        "home.html",
        get_page_context()
    )


def documentation(request):

    return render(
        request,
        "documentation.html",
        get_page_context()
    )


def templates(request):

    return render(
        request,
        "templates.html",
        get_page_context()
    )


def how_it_works(request):

    return render(
        request,
        "how_it_works.html",
        get_page_context()
    )


def research(request):

    return render(
        request,
        "research.html",
        get_page_context()
    )


def contribute(request):

    return render(
        request,
        "contribute.html",
        get_page_context()
    )


def blog(request):

    return render(
        request,
        "blog.html",
        get_page_context()
    )


def about(request):

    return render(
        request,
        "about.html",
        get_page_context()
    )