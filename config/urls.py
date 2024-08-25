from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("link_page.urls")), 
    path("accounts/", include("accounts.urls")),
    path("", include("django.contrib.auth.urls")), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
