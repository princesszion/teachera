# nominations_awards/admin.py

from django.contrib import admin
from .models import Nomination

@admin.register(Nomination)
class NominationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nominee_name",
        "category",
        "nominee_institution",
        "submitted_at",
        "approved",
        "photo",
    )
    list_filter = ("category", "approved", "submitted_at")
    search_fields = (
        "nominee_name",
        "nominee_email",
        "nominee_institution",
        "nominated_by_name",
        "nominated_by_email",
    )
    date_hierarchy = "submitted_at"
    ordering = ("-submitted_at",)

    # allow the admin list view to toggle 'approved' directly
    list_editable = ("approved",)
