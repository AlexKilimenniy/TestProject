from rest_framework import viewsets
from blog.models import *
from api.serializers import *

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostMessageViewSet(viewsets.ModelViewSet):
    queryset = PostMessage.objects.all().order_by('-id')
    serializer_class = PostMessageSerializer

    # def get_all(self, request):
    #
    #     return queryset, serializer_class
    #
    # def get_post(self, request, post_pk):
    #     queryset = PostMessage.objects.all()
    #     serializer_class = PostMessageSerializer
    #     return
