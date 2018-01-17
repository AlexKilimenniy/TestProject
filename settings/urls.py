from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views

from blog.api.urls import router as api_route
from blog import urls as blog_urls
from blog.views import UserCreateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^accounts/login/$', auth_views.login, {'template_name': 'account_temp/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout_then_login, name='logout'),
    url(r'^sign-up/$', UserCreateView.as_view(), name='signup'),

    #API
    url(r'^api/', include(api_route.urls)),

    #Blog
    url(r'^blog/', include(blog_urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

