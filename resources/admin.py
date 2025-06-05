# resources/admin.py

from django.contrib import admin
from .models import Resource, ResourcePurchase

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "uploader_name", "created_at")
    search_fields = ("title", "description", "uploader_name", "uploader_email")
    list_filter = ("price", "created_at")
    date_hierarchy = "created_at"
    ordering = ("-created_at",)


@admin.register(ResourcePurchase)
class ResourcePurchaseAdmin(admin.ModelAdmin):
    list_display = ("resource", "buyer_name", "buyer_email", "purchased_at")
    search_fields = ("resource__title", "buyer_name", "buyer_email", "transaction_id")
    list_filter = ("purchased_at",)
    date_hierarchy = "purchased_at"
    ordering = ("-purchased_at",)
