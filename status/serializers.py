from rest_framework import serializers
from .models import Status


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
            'id',
            'user',
            'content',
            'image',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['user']  # GET

    def validate_content(self, value):
        if len(value) > 1000:
            raise serializers.ValidationError('Content is Too long')
        return value

    def validate(self, data):
        content = data.get('content', None)
        if content == "":
            content = None
        image = data.get('image', None)
        if content is None and image is None:
            raise serializers.ValidationError('Content or Image is required')
        return data


