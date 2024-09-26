from rest_framework import serializers
from .models import Content
from django.contrib.auth import get_user_model

class ContentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Content
    fields = (
      "id",
      "owner",
      "body",
    )

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = get_user_model()
    fields = ("id", "username",)