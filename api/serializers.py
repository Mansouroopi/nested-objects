from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Post, Comment, Category


class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'owner', 'posts']
        depth = 1


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = ['id', 'body', 'owner', 'post']
        depth = 1


class UserSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)  # serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    categories = CategorySerializer(many=True)  # serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'comments', 'categories']
        depth = 1


class PostSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    owner = serializers.ReadOnlyField(source='owner.username')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'owner', 'comments', 'categories']
        extra_kwargs = {'categories': {'required': False}}
        depth = 1

    def update(self, instance, validated_data):
        # return HttpResponse(instance)
        print(validated_data)
        print(validated_data)
        categories = validated_data.pop('categories')
        instance.title = validated_data.get("title", instance.title)
        instance.body = validated_data.get("body", instance.body)
        instance.save()
        keep_categories = []
        for category in categories:
            if "id" in category.keys():
                if Category.objects.filter(id=category["id"]).exists():
                    c = Category.objects.get(id=category["id"])
                    c.text = category.get('text', c.text)
                    c.save()
                    keep_categories.append(c.id)
                else:
                    continue
            else:
                c = Category.objects.create(**category, post=instance)
                keep_categories.append(c.id)

        for category in instance.categories:
            if category.id not in keep_categories:
                category.delete()

        return instance




