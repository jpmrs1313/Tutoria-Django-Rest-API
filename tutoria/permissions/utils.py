from rest_framework.permissions import BasePermission
from permissions.models import RolePolicy, Policy
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group

HTTPDictionary = {
    "GET": "read",
    "POST": "create",
    "PUT": "update",
    "PATCH": "update",
    "DELETE": "delete",
}


class HasPermission(BasePermission):
    def has_permission(self, request, view):
        operation = HTTPDictionary[request.method]
        content_type = ContentType.objects.get_for_model(view.queryset.model)
        group = Group.objects.get(name=request.user.group)

        policy = Policy.objects.get(Operation=operation, ContentType=content_type.id)
        HasPermission = RolePolicy.objects.filter(
            policy=policy.id, group=group.id
        ).exists()

        return HasPermission
