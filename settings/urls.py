"""TestProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from blog import views

from django.contrib.auth import views as auth

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.BlogHomePage, name='blog'),

    url(r'^login/$', auth.login, {'template_name': 'login/login.html'}, name='sig-in'),
    url(r'^logout/$', auth.logout, {'next_page': '/'}, name='sig-out'),
    url(r'^blog/$', views.BlogHome, name='blog-home'),

    url(r'^sign-up/$', views.BlogSignUp, name='blog-signup'),

    url(r'^postcreate/$', views.CreatePost, name='create_post'),
    url(r'^commentcreate/(?P<pk>-?\d+)/$', views.CreateComment, name='create_comment'),
]
