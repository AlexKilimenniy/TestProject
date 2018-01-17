from django.conf.urls import url
from blog.views import PostsListView, PostCreateView, CommentCreateView

urlpatterns = [
    url(r'^$', PostsListView.as_view(), name='blog'),
    url(r'^post/create/$', PostCreateView.as_view(), name='create_post'),
    url(r'^comment/add/(?P<pk>-?\d+)/$', CommentCreateView.as_view(), name='new_comment'),
]