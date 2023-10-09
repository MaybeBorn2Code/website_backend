# DRF
from rest_framework import serializers
# Local
from .models import (
    Categories,
    Projects,
)
# Python
from typing import Any


class CategoriesSerializer(serializers.ModelSerializer):
    """Category serializer."""

    class Meta:
        model = Categories
        fields = '__all__'

    def create(self, validated_data: dict[str, Any]) -> Categories:
        """
        Create and return a new Categories instance, given the validated data.
        """
        categories: Categories = Categories.objects.create(
            **validated_data
        )
        return categories


class ProjectsSerializer(serializers.ModelSerializer):
    """Project serializer."""

    class Meta:
        model = Projects
        fields = '__all__'

    def create(self, validated_data: dict[str, Any]) -> Projects:
        """
        Create and return a new Projects instance, given the validated data.
        """
        projects: Projects = Projects.objects.create(
            **validated_data
        )
        return projects
