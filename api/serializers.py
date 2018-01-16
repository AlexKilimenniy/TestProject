from blog.models import PostMessage
from rest_framework import serializers
from django.contrib.auth.models import User


class PostMessageSerializer(serializers.ModelSerializer):
    massage_header = serializers.CharField(source='post_title')
    massage_body = serializers.CharField(source='post_text')

    class Meta:
        model = PostMessage
        fields = ('url', 'id', 'massage_header', 'massage_body', 'post_date', 'post_user', 'post_likes')


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'email', 'is_staff')