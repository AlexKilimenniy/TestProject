from django.contrib.auth.models import User
from rest_framework import viewsets

from blog.api.serializers import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostMessageViewSet(viewsets.ModelViewSet):
    queryset = PostMessage.objects.all().order_by('-id')
    serializer_class = PostMessageSerializer
