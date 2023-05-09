from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType
from .models import Policy


class ContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentType
        fields = ["app_label", "model", "name"]


class PolicySerializer(serializers.ModelSerializer):
    contenttype = serializers.CharField(source="ContentType.name")

    class Meta:
        model = Policy
        fields = ["Operation", "contenttype"]
