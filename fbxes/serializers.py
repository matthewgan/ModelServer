from rest_framework import serializers

from .models import Fbx


class FbxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fbx
        fields = "__all__"
        read_only_fields = ('created', 'updated', 'owner')
