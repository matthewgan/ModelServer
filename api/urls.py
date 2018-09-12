from rest_framework.routers import DefaultRouter
from categories.views import CategoryViewSet, CategoryByOwnerViewSet
from assetbundles.views import AssetBundleViewSet, AssetBundleByOwnerViewSet
from fbxes.views import FbxViewSet, FbxByOwnerViewSet


router = DefaultRouter()
router.register(r'categories', CategoryViewSet, base_name='categories')
router.register(r'category', CategoryByOwnerViewSet, base_name='category')
router.register(r'assetbundles', AssetBundleViewSet, base_name='assetbundles')
router.register(r'assetbundle', AssetBundleByOwnerViewSet, base_name='assetbundle')
router.register(r'fbxes', FbxViewSet, base_name='fbxes')
router.register(r'fbx', FbxByOwnerViewSet, base_name='fbx')

urlpatterns = router.urls
