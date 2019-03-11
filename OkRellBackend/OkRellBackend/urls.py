"""
OkRell Backend URL Configuration, include every apps urlpatterns 
corresponding to the identifying url for that view. 
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from Accounts import urls as accountUrls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include(accountUrls)),
    # url(r'^.*$', TemplateView.as_view(template_name='index.html')),
]

urlpatterns += static('/static', document_root=settings.STATIC_ROOT)
urlpatterns += static('/js', document_root=settings.JS_ROOT)
urlpatterns += static('/css', document_root=settings.CSS_ROOT)
urlpatterns += static('/img', document_root=settings.IMG_ROOT)
urlpatterns += static('/media', document_root=settings.MEDIA_ROOT)
