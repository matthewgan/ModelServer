from rest_framework.viewsets import ModelViewSet

from .models import Fbx
from .serializers import FbxSerializer


class FbxViewSet(ModelViewSet):
    queryset = Fbx.objects.all()
    serializer_class = FbxSerializer
