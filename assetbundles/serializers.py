from rest_framework import serializers
# from rest_framework.fields import CurrentUserDefault
from .models import AssetBundle


class AssetBundleSerializer(serializers.ModelSerializer):

    class Meta:
        model = AssetBundle
        # fields = "__all__"
        read_only_fields = ('created', 'updated', )
        exclude = ('isPublic', 'owner', )
