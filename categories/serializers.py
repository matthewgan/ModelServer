from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ('created', 'updated', 'owner')
