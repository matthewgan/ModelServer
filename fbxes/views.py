from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import AnonymousUser

from .models import Fbx
from .serializers import FbxSerializer


class FbxViewSet(ModelViewSet):
    queryset = Fbx.objects.all()
    serializer_class = FbxSerializer

    def perform_create(self, serializer):
        if type(self.request.user) == AnonymousUser:
            serializer.save()
        else:
            serializer.save(owner=self.request.user)
