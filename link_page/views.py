from django.conf import settings
from django.shortcuts import render


def linkpage(request):
    info: dict = getattr(settings, "INFO", None)
    return render(request, "link_page/frontpage.html", info)