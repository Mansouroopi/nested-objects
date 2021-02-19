from rest_framework import generics
from .models import Status
from .serializers import StatusSerializer
from django.views.decorators.csrf import csrf_exempt


# @csrf_exempt
class StatusList(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    model = Status
    serializer_class = StatusSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # def perform_update(self, serialize):
    #     pass
    #     # perform log or email

    # def get_queryset(self):
    #     qs = Status.objects.all()
    #     query = self.request.GET.get('q')
    #     if query is not None:
    #         return qs.filter(content__icontains=query)
    #     return qs


class StatusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    model = Status
    serializer_class = StatusSerializer
    # lookup_field = 'id'
    #
    # def get_object(self, *args, **kwargs):
    #     kwargs = self.kwargs
    #     kw_id = kwargs.get('id')
    #     return Status.objects.get(id=kw_id)

