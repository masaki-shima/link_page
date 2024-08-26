from django.conf import settings
from django.shortcuts import render
from django.views import View


class MoveSiteView(View):
    def get(self, request):
        # info.ymlの辞書型データを取得
        info: dict = getattr(settings, "INFO", None)
        return render(request, "move_site/index.html", {"info": info})       

movesite = MoveSiteView.as_view()