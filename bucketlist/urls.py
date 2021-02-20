from django.urls import path
from .views import DetailsView, CreateView


urlpatterns = [
    path('', CreateView.as_view(), name="create"),
    path('<int:pk>/', DetailsView.as_view(), name="details"),
]
