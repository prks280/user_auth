from rest_framework import routers

from .views import NetaViewSet, UserViewSet, RatingViewSet

router = routers.DefaultRouter()

router.register('neta', NetaViewSet)
router.register('user', UserViewSet)
router.register('rating', RatingViewSet)
# router.register('template', MyView)


urlpatterns = router.urls