
from django.contrib import admin
from django.urls import path,include,re_path
from django.urls import re_path as url

from django.views.generic import TemplateView
from propertystore import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("admin/", admin.site.urls),
    path('account/', include('accounts.urls')),
    path("accounts/", include("allauth.urls")),
    path('', views.home, name='home'),
    path('store/',include("propertystore.urls")),





]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
