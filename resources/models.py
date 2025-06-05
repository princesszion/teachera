# resources/models.py

import os
from django.db import models
from django.utils.text import slugify

def resource_file_upload_path(instance, filename):
    """
    Generates upload path: MEDIA_ROOT/resources/<year>/<month>/<resource_id>/<original_filename>
    """
    base, ext = os.path.splitext(filename)
    return f"resources/{instance.id}/{slugify(base)}{ext}"

class Resource(models.Model):
    """
    A file-based teaching resource that anyone can upload.
    """
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to=resource_file_upload_path)
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0.00,
        help_text="Enter 0.00 if this resource is free"
    )
    uploader_name = models.CharField(
        max_length=150,
        blank=True,
        help_text="Name of the person who uploaded this resource (e.g. Teacher’s name)"
    )
    uploader_email = models.EmailField(
        blank=True,
        help_text="Email address of the uploader (optional)"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} (₵{self.price})"


class ResourcePurchase(models.Model):
    """
    Record of someone “purchasing” a resource. Since we don't have a User model,
    we store buyer_name and buyer_email as plain fields for now.
    """
    resource = models.ForeignKey(
        Resource, on_delete=models.CASCADE, related_name="purchases"
    )
    buyer_name = models.CharField(max_length=150)
    buyer_email = models.EmailField()
    purchased_at = models.DateTimeField(auto_now_add=True)
    # In a real payment integration, you'd store a transaction_id or receipt here:
    transaction_id = models.CharField(
        max_length=100,
        blank=True,
        help_text="Optional: payment transaction reference"
    )

    def __str__(self):
        return f"{self.buyer_name} bought {self.resource.title} on {self.purchased_at:%Y-%m-%d}"
