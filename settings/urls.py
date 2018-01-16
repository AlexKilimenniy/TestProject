from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from blog import views
from api.urls import router as api_route
from django.contrib.auth import views as auth


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', views.BlogHomePage, name='blog'),

    url(r'^login/$', auth.login, {'template_name': 'login/login.html'}, name='sig-in'),
    url(r'^logout/$', auth.logout, {'next_page': '/'}, name='sig-out'),
    url(r'^sign-up/$', views.BlogSignUp, name='blog-signup'),

    url(r'^blog/$', views.BlogHome, name='blog-home'),
    url(r'^postcreate/$', views.CreatePost, name='create_post'),
    url(r'^commentcreate/(?P<pk>-?\d+)/$', views.CreateComment, name='create_comment'),

    # API
    url(r'^api/', include(api_route.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

