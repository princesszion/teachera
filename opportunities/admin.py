# # opportunities/admin.py

# from django.contrib import admin
# from .models import Category, Opportunity

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ("name", "slug")
#     search_fields = ("name",)


# @admin.register(Opportunity)
# # class OpportunityAdmin(admin.ModelAdmin):
# #     list_display = ("title", "category", "opportunity_type", "post_date", "is_active")
# #     list_filter = ("opportunity_type", "is_active", "category")
# #     search_fields = ("title", "description", "location")
# #     date_hierarchy = "post_date"
# #     ordering = ("-post_date",)
# class OpportunityAdmin(admin.ModelAdmin):
#     list_display = ("title", "category","post_date", "is_active")
#     list_filter = ( "is_active", "category")
#     search_fields = ("title", "description", "location")
#     date_hierarchy = "post_date"
#     ordering = ("-post_date",)

# from django.contrib import admin
# from django.db import models
# from django_ckeditor_5.widgets import CKEditor5Widget
# from .models import Category, Opportunity

# # Apply CKEditor5 globally only to TextFields
# admin.site.formfield_overrides = {
#     models.TextField: {'widget': CKEditor5Widget(config_name='default')},
# }

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ("name", "slug")
#     search_fields = ("name",)


# @admin.register(Opportunity)
# class OpportunityAdmin(admin.ModelAdmin):
#     list_display = ("title", "category", "post_date", "is_active")
#     list_filter = ("is_active", "category")
#     search_fields = ("title", "description", "location")
#     date_hierarchy = "post_date"
#     ordering = ("-post_date",)



from django import forms
from django.contrib import admin
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Opportunity, Category

class OpportunityForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditor5Widget(config_name='default'))
    eligibility = forms.CharField(widget=CKEditor5Widget(config_name='default'))
    benefits = forms.CharField(widget=CKEditor5Widget(config_name='default'))
    process = forms.CharField(widget=CKEditor5Widget(config_name='default'))

    class Meta:
        model = Opportunity
        fields = "__all__"

@admin.register(Opportunity)
class OpportunityAdmin(admin.ModelAdmin):
    form = OpportunityForm
    list_display = ("title", "category", "post_date", "is_active")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
