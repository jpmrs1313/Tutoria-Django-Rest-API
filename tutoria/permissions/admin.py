from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from .models import Policy


@admin.register(ContentType)
class ContentTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    pass
