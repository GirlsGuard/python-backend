from django.urls import path
from .views import *

urlpatterns = [
    path("homepage/", PostListCreateView.as_view(), name="homepage"),
    path("homepage/<int:pk>/", PostRetrieveUpdateDeleteView.as_view(), name="homepage")
]

