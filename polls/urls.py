from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^home/$', views.index, name='index'),
    url(r'^products/$', views.products, name='products'),
    url(r'^about/$', views.about, name='about'),
    url(r'^login/$', views.login, name='login')
]