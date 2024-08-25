from datetime import datetime
from zoneinfo import ZoneInfo

from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# LoginRequiredMixinはログインしていないとアクセスできない
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import FormView

from .forms import PageForm
from .models import Page


class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        # 現在の日時を表示
        datetime_now: str = datetime.now(
            ZoneInfo("Asia/Tokyo")
        ).strftime("%Y年%m月%d日 %H:%M:%S")
        # info.ymlの辞書型データを取得
        info: dict = getattr(settings, "INFO", None)
        return render(request, "link_page/index.html", {**info, "datetime_now": datetime_now})       
        
# コメントや画像を投稿
class PageCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = PageForm()
        return render(request, "link_page/page_form.html", {"form": form})
    
    def post(self, request):
        # データを画像も含めて登録
        form = PageForm(request.POST, request.FILES)
        if form.is_valid():
            form. save()
            return redirect("link_page:index")
        return render(request, "link_page/page_form.html", {"form": form})

# コメントされたタイトル閲覧
class CommentListView(LoginRequiredMixin, View):
    def get(self, request):
        # order_byで昇順。フィールド名の先頭に-をつけると降順。
        comment_list = Page.objects.order_by("-page_date")
        return render(request, "link_page/comment_list.html", {"comment_list": comment_list})

# コメントされた内容閲覧
class CommentDetailView(LoginRequiredMixin, View):
    def get(self, request, id):
        # データベースから同じidを持つコメントを取得
        comment = get_object_or_404(Page, id=id)
        return render(request, "link_page/comment_detail.html", {"comment": comment})

# コメントした内容の更新
class CommentUpdateView(LoginRequiredMixin, View):
    def get(self, request, id):
        # データベースから同じidを持つコメントを取得
        comment = get_object_or_404(Page, id=id)
        # もともと登録されていたデータをFormに含める
        form = PageForm(instance=comment)
        return render(request, "link_page/comment_update.html", {"form": form})
        
    # 更新したコメントを登録する
    def post(self, request, id):
        page = get_object_or_404(Page, id=id)
        form = PageForm(request.POST, request.FILES, instance=page)
        if form.is_valid():
            form.save()
            return redirect("link_page:comment_detail", id=id)
        return render(request, "link_page/comment_form.html", {"form": form})

# コメントを削除
class CommentDeleteView(LoginRequiredMixin, View):
    def get(self, request, id):
        comment = get_object_or_404(Page, id=id)
        return render(request, "link_page/comment_delete.html", {"comment": comment})

    def post(self, request, id):
        comment = get_object_or_404(Page, id=id)
        comment.delete()
        return redirect('link_page:comment_list')
             

index = IndexView.as_view()
page_create = PageCreateView.as_view()
comment_list = CommentListView.as_view()
comment_detail = CommentDetailView.as_view()
comment_update = CommentUpdateView.as_view()
comment_delete = CommentDeleteView.as_view()


# DBを使わないページ
class DropdownView00(LoginRequiredMixin, View):
    def get(self, request):
        # 現在の日時を表示
        datetime_now: str = datetime.now(
            ZoneInfo("Asia/Tokyo")
        ).strftime("%Y年%m月%d日 %H:%M:%S")
        # info.ymlの辞書型データを取得
        info: dict = getattr(settings, "INFO", None)
        return render(request, "link_page/test/dropdown00.html", {**info, "datetime_now": datetime_now})

class DropdownView01(LoginRequiredMixin, View):
    def get(self, request):
        datetime_now: str = datetime.now(
            ZoneInfo("Asia/Tokyo")
        ).strftime("%Y年%m月%d日 %H:%M:%S")
        info: dict = getattr(settings, "INFO", None)
        return render(request, "link_page/test/dropdown01.html", {**info, "datetime_now": datetime_now})

class jQueryView(LoginRequiredMixin, View):
    def get(self, request):
        datetime_now: str = datetime.now(
            ZoneInfo("Asia/Tokyo")
        ).strftime("%Y年%m月%d日 %H:%M:%S")
        info: dict = getattr(settings, "INFO", None)
        return render(request, "link_page/test/jquery.html", {**info, "datetime_now": datetime_now})
    
class TestView(LoginRequiredMixin, View):
    def get(self, request):
        datetime_now: str = datetime.now(
            ZoneInfo("Asia/Tokyo")
        ).strftime("%Y年%m月%d日 %H:%M:%S")
        info: dict = getattr(settings, "INFO", None)
        return render(request, "link_page/test/test.html", {**info, "datetime_now": datetime_now})

