from django.shortcuts import render


def linkpage(request):
    return render(request, "link_page/frontpage.html")