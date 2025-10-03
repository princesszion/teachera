# nominations_awards/models.py

from django.db import models

class Nomination(models.Model):
    """
    Represents a nomination for a teacher award or recognition.
    Fields:
      - nominee_name: name of the teacher being nominated
      - nominee_email: email of the nominee (optional, if you wish to contact them)
      - nominee_institution: institution or school where the nominee teaches
      - category: type of nomination (e.g., Teacher of the Month, Teacher of the Year)
      - rationale: why this nominee deserves the award
      - nominated_by_name: who is submitting the nomination
      - nominated_by_email: their contact (optional)
      - submitted_at: timestamp when the nomination was created
      - approved: whether an admin has approved this nomination (default=False)
    """

    TEACHER_OF_MONTH = "Teacher of the Month"
    TEACHER_OF_YEAR = "Teacher of the Year"
    OTHER = "Other"

    CATEGORY_CHOICES = [
        (TEACHER_OF_MONTH, "Teacher of the Month"),
        (TEACHER_OF_YEAR, "Teacher of the Year"),
        (OTHER, "Other"),
    ]

    nominee_name = models.CharField(max_length=200)
    nominee_email = models.EmailField(
        blank=True,
        help_text="(Optional) Email address of the nominee"
    )
    nominee_institution = models.CharField(
        max_length=200,
        help_text="Institution or school where the nominee teaches"
    )
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default=TEACHER_OF_MONTH,
        help_text="Select the nomination category"
    )
    rationale = models.TextField(
        help_text="Explain why this teacher deserves the recognition"
    )
    nominated_by_name = models.CharField(
        max_length=150,
        help_text="Name of the person making this nomination"
    )
    nominated_by_email = models.EmailField(
        blank=True,
        help_text="(Optional) Contact email of the nominator"
    )
    submitted_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(
        default=False,
        help_text="Set to True once an admin approves this nomination"
    )
    photo = models.ImageField(
        upload_to="nominations/",
        blank=True,
        null=True,
        help_text="Upload a photo for Teacher of the Month/Year"
    )
    class Meta:
        ordering = ["-submitted_at"]

    def __str__(self):
        return f"{self.nominee_name} nominated by {self.nominated_by_name} ({self.category})"
