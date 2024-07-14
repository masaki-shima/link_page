from django.shortcuts import render

def frontpage(request):
    return render(request, "link_page/frontpage.html")