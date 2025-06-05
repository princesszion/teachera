# opportunities/admin.py

from django.contrib import admin
from .models import Category, Opportunity

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name",)


@admin.register(Opportunity)
class OpportunityAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "opportunity_type", "post_date", "is_active")
    list_filter = ("opportunity_type", "is_active", "category")
    search_fields = ("title", "description", "location")
    date_hierarchy = "post_date"
    ordering = ("-post_date",)
