# feedback_discussion/models.py

from django.db import models

class Feedback(models.Model):
    """
    General feedback submitted by anyone.
    Fields:
      - name: optional name of the submitter
      - email: optional email of the submitter (for follow-up)
      - content: the feedback text
      - created_at: timestamp when feedback was submitted
    """
    name = models.CharField(
        max_length=150,
        blank=True,
        help_text="(Optional) Your name"
    )
    email = models.EmailField(
        blank=True,
        help_text="(Optional) Your email address"
    )
    content = models.TextField(
        help_text="Your feedback or prompt for TeachEra"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        display_name = self.name if self.name else "Anonymous"
        return f"Feedback by {display_name} on {self.created_at:%Y-%m-%d %H:%M}"


class DiscussionComment(models.Model):
    """
    A threaded comment in the discussion box. Anyone can post.
    Fields:
      - name: optional name of the commenter
      - email: optional email of the commenter
      - body: the comment text
      - parent: self-referential FK for nested replies (null for top-level)
      - created_at: timestamp when comment was posted
    """
    name = models.CharField(
        max_length=150,
        blank=True,
        help_text="(Optional) Your name (leave blank to post as Anonymous)"
    )
    email = models.EmailField(
        blank=True,
        help_text="(Optional) Your email (not displayed publicly)"
    )
    body = models.TextField(
        help_text="Your comment or reply"
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="replies",
        help_text="(Optional) If this is a reply, select the parent comment"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]  # oldest first; adjust if you want newest first

    def __str__(self):
        display_name = self.name if self.name else "Anonymous"
        return f"Comment by {display_name} on {self.created_at:%Y-%m-%d %H:%M}"
