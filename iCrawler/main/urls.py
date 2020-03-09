from django.conf import settings
from django.conf.urls import url,static
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    #url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^api/crawl/', views.crawl, name='crawl'),
    url(r'home', views.home, name='home'),
    url(r'fetch', views.fetch, name='fetch'),
    url(r'data', views.data, name='data'),
]

# This is required for static files while in development mode. (DEBUG=TRUE)
# No, not relevant to scrapy or crawling :)

