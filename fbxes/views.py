from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import AnonymousUser
from rest_framework.permissions import IsAuthenticated

from .models import Fbx
from .serializers import FbxSerializer
from api.filters import IsOwnerFilterBackend


class FbxViewSet(ModelViewSet):
    queryset = Fbx.objects.all()
    serializer_class = FbxSerializer

    def perform_create(self, serializer):
        if type(self.request.user) == AnonymousUser:
            serializer.save()
        else:
            serializer.save(owner=self.request.user)


class FbxByOwnerViewSet(ModelViewSet):
    queryset = Fbx.objects.all()
    serializer_class = FbxSerializer
    filter_backends = (IsOwnerFilterBackend, )
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
