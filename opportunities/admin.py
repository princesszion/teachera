
from django.contrib import admin
from django.db import models
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Opportunity, Category

@admin.register(Opportunity)
class OpportunityAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "post_date", "is_active")

    formfield_overrides = {
        models.TextField: {"widget": CKEditor5Widget(config_name="default")},
        # models.CharField: {"widget": CKEditor5Widget(config_name="default")},
    }

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")


# from django import forms
# from django.contrib import admin
# from django_ckeditor_5.widgets import CKEditor5Widget
# from .models import Opportunity, Category

# class OpportunityForm(forms.ModelForm):
#     description = forms.CharField(widget=CKEditor5Widget(config_name='default'))
#     eligibility = forms.CharField(widget=CKEditor5Widget(config_name='default'))
#     benefits = forms.CharField(widget=CKEditor5Widget(config_name='default'))
#     process = forms.CharField(widget=CKEditor5Widget(config_name='default'))

#     class Meta:
#         model = Opportunity
#         fields = "__all__"

# @admin.register(Opportunity)
# class OpportunityAdmin(admin.ModelAdmin):
#     form = OpportunityForm
#     list_display = ("title", "category", "post_date", "is_active")

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ("name", "slug")
