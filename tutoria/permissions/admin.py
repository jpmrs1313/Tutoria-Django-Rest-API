from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from .models import Policy, RolePolicy


@admin.register(ContentType)
class ContentTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    pass


@admin.register(RolePolicy)
class RolePolicyAdmin(admin.ModelAdmin):
    pass
