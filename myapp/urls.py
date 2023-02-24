from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from tickets import views
from django.views.static import serve
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('zealadmin/', admin.site.urls),
    path('ticket/', include('tickets.urls')),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('submit', views.submit, name="submit"),
    re_path(r'^media/(?P<path>.*)$', serve,
            {'document_root':       settings.MEDIA_ROOT}),
    re_path(r'^assets/(?P<path>.*)$', serve,
            {'document_root': settings.STATIC_ROOT}),
]
