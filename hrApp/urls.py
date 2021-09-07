from django.conf.urls import url
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve 

from . import views

app_name="hrApp"

urlpatterns = [
    # url(r'^$',indexPage,name='indexPage'),
    path('', views.indexPage, name='indexPage'),

#     url(r'^property/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),     
#     url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
# ]
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)