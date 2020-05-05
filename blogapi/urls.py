from rest_framework.routers import DefaultRouter

from .views import BlogViewSet

router = DefaultRouter()
# router.register(r'blogs', BlogView, basename='user')
router.register(r'blogs', BlogViewSet, basename='user')

urlpatterns = router.urls
