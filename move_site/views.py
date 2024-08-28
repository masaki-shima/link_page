from django.conf import settings
from django.shortcuts import render
from django.views import View


class MoveSiteView(View):
    def get(self, request):
        # info.ymlの辞書型データを取得
        info: dict = getattr(settings, "INFO", None)
        return render(request, "move_site/index.html", {"info": info})       

class ScrollView(View):
    def get(self, request):
        # info.ymlの辞書型データを取得
        info: dict = getattr(settings, "INFO", None)
        return render(request, "move_site/scroll.html", {"info": info})       

class ScrollAnimationView(View):
    def get(self, request):
        # info.ymlの辞書型データを取得
        info: dict = getattr(settings, "INFO", None)
        return render(request, "move_site/scroll_animation.html", {"info": info})       

class BootstrapView(View):
    def get(self, request):
        # info.ymlの辞書型データを取得
        info: dict = getattr(settings, "INFO", None)
        return render(request, "move_site/bootstrap.html", {"info": info})       

movesite = MoveSiteView.as_view()
scroll = ScrollView.as_view()
scroll_animation = ScrollAnimationView.as_view()
bootstrap = BootstrapView.as_view()
