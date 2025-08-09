# opportunities/models.py

from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    """
    A high‐level grouping for opportunities:
    e.g. 'Jobs', 'Internships', 'Volunteer', 'Scholarships', 'Training'
    """
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)

    def save(self, *args, **kwargs):
        # Auto‐generate slug from name if not provided
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Opportunity(models.Model):
    """
    An individual opportunity listing.
    """
    JOB = "job"
    INTERNSHIP = "internship"
    VOLUNTEER = "volunteer"
    SCHOLARSHIP = "scholarship"
    TRAINING = "training"
    FELLOWSHIP = "fellowship"

    OPPORTUNITY_CHOICES = [
        (JOB, "Full‐Time Job"),
        (INTERNSHIP, "Internship"),
        (VOLUNTEER, "Volunteer"),
        (SCHOLARSHIP, "Scholarship"),
        (FELLOWSHIP, "Fellowship"),
        (TRAINING, "Training/Online Course"),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    organization = models.CharField(max_length=255, blank=True, help_text="(optional) Company or Organization Name")
    deadline = models.DateTimeField()
    instructions = models.TextField(
        help_text="How to apply or get involved. Include links if applicable."
    )
    post_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="opportunities"
    )
    opportunity_type = models.CharField(
        max_length=50,
        choices=OPPORTUNITY_CHOICES,
        help_text="Choose one of: job, internship, volunteer, scholarship, training",
    )
    location = models.CharField(
        max_length=150, blank=True, help_text="(optional) City, Country, or Online"
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} ({self.get_opportunity_type_display()})"

