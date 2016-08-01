"""pi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout
from core.views import Home, PostDetail, Berita, Fiksi, register, Olahraga, Teknologi, redirect_to_home

urlpatterns = [
    url(r'^grappeli/', include('grappelli.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', Home.as_view(), name='home'),
    url(r'^post/(?P<pk>\d+)/$', PostDetail.as_view(), name='post_detail'),
    url(r'^fiksi/$', Fiksi.as_view(), name='fiksi'),
    url(r'^berita/$', Berita.as_view(), name='berita'),
    url(r'^olahraga/$', Olahraga.as_view(), name='olahraga'),
    url(r'^teknologi/$', Teknologi.as_view(), name='teknologi'),
    url(r'^registration/$', register),
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout),
]
