from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("AJ_Tours_and_Travels/", include("AJ_Tours_and_Travels.urls")),
    path("", include("AJ_Tours_and_Travels_API.urls")),
    path("admin/", admin.site.urls),
] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

