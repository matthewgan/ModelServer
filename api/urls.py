from rest_framework.routers import DefaultRouter
from categories.views import CategoryViewSet, CategoryByOwnerViewSet
from assetbundles.views import AssetBundleViewSet
from fbxes.views import FbxViewSet


router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'category', CategoryByOwnerViewSet)
router.register(r'assetbundles', AssetBundleViewSet)
router.register(r'fbxes', FbxViewSet)

urlpatterns = router.urls
