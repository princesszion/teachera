# feedback_discussion/urls.py

from django.urls import path, include
from rest_framework import routers
from .views import FeedbackViewSet, DiscussionCommentViewSet

router = routers.DefaultRouter()
router.register(r"feedbacks", FeedbackViewSet, basename="feedback")
router.register(r"comments", DiscussionCommentViewSet, basename="comment")

urlpatterns = [
    path("", include(router.urls)),
]
