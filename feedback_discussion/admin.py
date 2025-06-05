# feedback_discussion/admin.py

from django.contrib import admin
from .models import Feedback, DiscussionComment

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "email", "created_at")
    search_fields = ("name", "email", "content")
    list_filter = ("created_at",)
    date_hierarchy = "created_at"
    ordering = ("-created_at",)

    def display_name(self, obj):
        return obj.name or "Anonymous"
    display_name.short_description = "Name"


@admin.register(DiscussionComment)
class DiscussionCommentAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "parent_id", "created_at")
    search_fields = ("name", "email", "body")
    list_filter = ("created_at",)
    date_hierarchy = "created_at"
    ordering = ("created_at",)

    def display_name(self, obj):
        return obj.name or "Anonymous"
    display_name.short_description = "Name"
