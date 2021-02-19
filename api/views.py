from django.http import HttpResponse
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.response import Response

from api import serializers
from api.models import Post, Comment, Category
from rest_framework import permissions
from api.permissions import IsOwnerOrReadOnly
from api.serializers import PostSerializer, CommentSerializer
# https://blog.logrocket.com/use-django-rest-framework-to-build-a-blog/


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def create(self, validated_data):
    #     choices = validated_data.pop('categories')
    #     tags = validated_data.pop('tags')
    #     question = Question.objects.create(**validated_data)
    #     for choice in choices:
    #         Choice.objects.create(**choice, question=question)
    #     question.tags.set(tags)
    #     return question

    def create(self, request, *args, **kwargs):
        post_data = request.data
        print(self.request.user)
        new_post = Post.objects.create(title=post_data['title'], body=post_data['body'], owner=self.request.user)

        # Get our categories
        category_data = post_data['categories'].split(',')

        for category in category_data:
            category = Category.objects.get(id=category)
            new_post.categories.add(category.id)

        new_post.save()
        serializer = PostSerializer(new_post)
        return Response(serializer.data)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                        #  IsOwnerOrReadOnly]


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        comment_data = request.data

        new_comment = Comment.objects.create(body=comment_data['body'],
                                             post=Post.objects.get(id=comment_data['post']),
                                             owner=self.request.user)
        new_comment.save()
        serializer = CommentSerializer(new_comment)
        return Response(serializer.data)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

