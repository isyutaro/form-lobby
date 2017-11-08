from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
from form_lobby import views

urlpatterns = [
    url(r'^$', views.lobby, name='lobby'),
    url(r'^gracias/', views.gracias, name='gracias'),
    url(r'^djmanager/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
