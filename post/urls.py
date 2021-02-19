from django.urls import path

from .views import PostListCreateAPIView, PostDetailsAPIView


from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
   openapi.Info(
      title="Blog API",
      default_version='v1',
      description="Test description",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view(), name='api-post-list'),
    path('posts/<int:pk>/', PostDetailsAPIView.as_view(), name='api-post-details'),
    path('doc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]