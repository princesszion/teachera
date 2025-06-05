# nominations_awards/urls.py

from django.urls import path, include
from rest_framework import routers
from .views import NominationViewSet

router = routers.DefaultRouter()
router.register(r"nominees", NominationViewSet, basename="nomination")

urlpatterns = [
    path("", include(router.urls)),
]
