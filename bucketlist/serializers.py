from rest_framework import serializers
from bucketlist.models import Bucketlist


class BucketlistSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance into json format."""

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Map this serializer to a model and their fields."""
        model = Bucketlist
        fields = ('id', 'name', 'owner', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')