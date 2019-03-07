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
from User import urls as userUrls
urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^$', TemplateView.as_view(template_name='index.html')),
    path('api/user/', include(userUrls))
]

urlpatterns += static('/js', document_root=settings.STATIC_ROOT)
urlpatterns += static('/css', document_root=settings.STATIC_ROOT)
urlpatterns += static('/img', document_root=settings.STATIC_ROOT)
urlpatterns += static('/media', document_root=settings.MEDIA_ROOT)
