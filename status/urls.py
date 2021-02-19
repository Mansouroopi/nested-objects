from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from status import views

urlpatterns = [
    path('', views.StatusList.as_view()),
    path('<int:pk>/', views.StatusDetail.as_view()),



]

urlpatterns = format_suffix_patterns(urlpatterns)