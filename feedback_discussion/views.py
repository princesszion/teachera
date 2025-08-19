# # feedback_discussion/views.py

# from rest_framework import viewsets, permissions, filters
# from .models import Feedback, DiscussionComment
# from .serializers import FeedbackSerializer, DiscussionCommentSerializer
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
# from rest_framework.views import APIView

# @method_decorator(csrf_exempt, name='dispatch')
# class FeedbackViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows anyone to list, create, retrieve, update, and delete Feedback.
#     """
#     queryset = Feedback.objects.all().order_by("-created_at")
#     serializer_class = FeedbackSerializer
#     permission_classes = [permissions.AllowAny]

#     filter_backends = [filters.SearchFilter, filters.OrderingFilter]
#     search_fields = ["name", "email", "content"]
#     ordering_fields = ["created_at"]


# class DiscussionCommentViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows anyone to list, create, retrieve, update, and delete DiscussionComment.
#     Nested replies are included in the serialized data.
#     """
#     queryset = DiscussionComment.objects.filter(parent__isnull=True).order_by("created_at")
#     # Only top‐level comments are returned by default; `replies` is nested in the serializer.
#     serializer_class = DiscussionCommentSerializer
#     permission_classes = [permissions.AllowAny]

#     filter_backends = [filters.SearchFilter, filters.OrderingFilter]
#     search_fields = ["name", "email", "body"]
#     ordering_fields = ["created_at"]

#     def get_queryset(self):
#         """
#         By default, return only top-level comments (parent is null).
#         To retrieve all comments (including replies) flatly, you could override this.
#         """
#         return DiscussionComment.objects.filter(parent__isnull=True).order_by("created_at")

from rest_framework import viewsets, permissions, filters
from .models import Feedback, DiscussionComment
from .serializers import FeedbackSerializer, DiscussionCommentSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name="dispatch")
class FeedbackViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows anyone to list, create, retrieve, update, and delete Feedback.
    """
    queryset = Feedback.objects.all().order_by("-created_at")
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.AllowAny]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name", "email", "content"]
    ordering_fields = ["created_at"]


@method_decorator(csrf_exempt, name="dispatch")
class DiscussionCommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows anyone to list, create, retrieve, update, and delete DiscussionComment.
    Nested replies are included in the serialized data.
    """
    queryset = DiscussionComment.objects.filter(parent__isnull=True).order_by("created_at")
    serializer_class = DiscussionCommentSerializer
    permission_classes = [permissions.AllowAny]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name", "email", "body"]
    ordering_fields = ["created_at"]

    def get_queryset(self):
        """
        By default, return only top-level comments (parent is null).
        """
        return DiscussionComment.objects.filter(parent__isnull=True).order_by("created_at")
