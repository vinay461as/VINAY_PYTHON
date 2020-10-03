from django.conf.urls import url, include
from django.views.generic import TemplateView

from mysite.routers import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^router/$', views.router_list, name='router_list'),
    url(r'^router/create/$', views.router_create, name='router_create'),
    url(r'^router/(?P<pk>\d+)/update/$', views.router_update, name='router_update'),
    url(r'^router/(?P<pk>\d+)/delete/$', views.router_delete, name='router_delete'),
]
