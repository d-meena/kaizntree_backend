from home.views import ProductViewSet, TagViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='user')
router.register(r'tags', TagViewSet, basename='tags')
urlpatterns = router.urls
