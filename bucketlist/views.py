from rest_framework import generics
from bucketlist.models import Bucketlist
from bucketlist.serializers import BucketlistSerializer
from rest_framework import permissions
from .permissions import IsOwner


class CreateView(generics.ListCreateAPIView):
    """This class handles the GET and POSt requests of our rest api."""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)  # IsAuthenticatedOrReadOnly

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save(owner=self.request.user)


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles GET, PUT, PATCH and DELETE requests."""

    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

