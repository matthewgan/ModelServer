from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import AnonymousUser

from .models import AssetBundle
from .serializers import AssetBundleSerializer


class AssetBundleViewSet(ModelViewSet):
    queryset = AssetBundle.objects.all()
    serializer_class = AssetBundleSerializer

    def perform_create(self, serializer):
        if type(self.request.user) == AnonymousUser:
            serializer.save()
        else:
            serializer.save(owner=self.request.user)
