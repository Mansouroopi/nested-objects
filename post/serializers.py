from rest_framework import serializers
from post.models import BlogPost as Post, Tag
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance into json format."""
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class TagSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance into json format."""
    class Meta:
        model = Tag
        fields = ['id', 'name']


class PostSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance into json format."""
    tags = TagSerializer(many=True, required=False, read_only=True)
    author = UserSerializer(read_only=True, required=False)
    serializers.ImageField(required=False, allow_null=True, use_url=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'text', 'image', 'created_at', 'tags', 'image', 'author']
