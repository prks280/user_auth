from rest_framework.routers import DefaultRouter
from .views import TestViewSet

router = DefaultRouter()
router.register('test',TestViewSet)

urlpatterns = router.urls