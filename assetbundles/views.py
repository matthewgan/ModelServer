from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import AnonymousUser
from rest_framework.permissions import IsAuthenticated

from .models import AssetBundle
from .serializers import AssetBundleSerializer
from api.filters import IsOwnerFilterBackend, IsOwnerOrPublicFilterBackend


class AssetBundleViewSet(ModelViewSet):
    queryset = AssetBundle.objects.all()
    serializer_class = AssetBundleSerializer

    def perform_create(self, serializer):
        if type(self.request.user) == AnonymousUser:
            serializer.save()
        else:
            serializer.save(owner=self.request.user)


class AssetBundleByOwnerViewSet(ModelViewSet):
    queryset = AssetBundle.objects.all()
    serializer_class = AssetBundleSerializer
    filter_backends = (IsOwnerOrPublicFilterBackend, )
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
