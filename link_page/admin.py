from django.contrib import admin

from .models import Page

# admin.site.register(Page)


@admin.register(Page)
# 管理画面でデフォルトで表示されない部分を表示
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ["id", "created_at", "updated_at"]