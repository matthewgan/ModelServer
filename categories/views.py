from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import AnonymousUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from django.http import Http404
from rest_framework.response import Response

from .models import Category
from .serializers import CategorySerializer
from api.filters import IsOwnerOrPublicFilterBackend
from assetbundles.models import AssetBundle
from assetbundles.serializers import AssetBundleSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        if type(self.request.user) == AnonymousUser:
            serializer.save()
        else:
            serializer.save(owner=self.request.user)

    @staticmethod
    def get_objects(pk):
        try:
            return AssetBundle.objects.filter(category=pk)
        except AssetBundle.DoesNotExist:
            return Http404

    @action(methods=['get'], detail=True,
            url_path='assetbundles', url_name='list_assetbundles')
    def list_assetbundles(self, request, pk, format=None):
        print(pk)
        assetbundles = self.get_objects(pk=pk)
        serializer = AssetBundleSerializer(assetbundles, many=True)
        return Response(serializer.data)


class CategoryByOwnerViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (IsOwnerOrPublicFilterBackend, )
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @staticmethod
    def get_objects(pk):
        try:
            return AssetBundle.objects.filter(category=pk)
        except AssetBundle.DoesNotExist:
            return Http404

    @action(methods=['get'], detail=True,
            url_path='assetbundles', url_name='list_assetbundles')
    def list_assetbundles(self, request, pk, format=None):
        print(pk)
        assetbundles = self.get_objects(pk=pk)
        serializer = AssetBundleSerializer(assetbundles, many=True)
        return Response(serializer.data)
