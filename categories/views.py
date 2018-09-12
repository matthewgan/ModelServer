from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import AnonymousUser

from .models import Category
from .serializers import CategorySerializer
from api.filters import IsOwnerFilterBackend, IsPublicFilterBackend, IsOwnerOrPublicFilterBackend


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        if type(self.request.user) == AnonymousUser:
            serializer.save()
        else:
            serializer.save(owner=self.request.user)


class CategoryByOwnerViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (IsOwnerOrPublicFilterBackend, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework import generics
# from rest_framework.response import Response
# from .models import Category
# from .serializers import CategorySerializer
# from assets.models import Asset
# from assets.serializers import AssetSerializer
#
#
# class CategoryListView(generics.ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
#
# class CategoryDetailView(APIView):
#     def get_objects(self, pk):
#         try:
#             return SubCategory.objects.filter(category=pk)
#         except SubCategory.DoesNotExist:
#             return Http404
#
#     def get(self, request, pk, format=None):
#         subs = self.get_objects(pk)
#         serializer = SubCategorySerializer(subs, many=True)
#         return Response(serializer.data)
#
#
# class SubCategoryDetailView(APIView):
#     def get_objects(self, pk):
#         try:
#             return Asset.objects.filter(subcategory=pk)
#         except Asset.DoesNotExist:
#             return Http404
#
#     def get(self, request, pk, format=None):
#         assets = self.get_objects(pk)
#         serializer = AssetSerializer(assets, many=True)
#         return Response(serializer.data)
