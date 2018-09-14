from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from .models import AssetBundle


class AssetBundleSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = AssetBundle
        # fields = "__all__"
        read_only_fields = ('created', 'updated', 'owner',)
        exclude = ('isPublic', )
