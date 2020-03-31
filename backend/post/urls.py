from rest_framework.routers import SimpleRouter

from .views import PostManager

router = SimpleRouter()
router.register('posts', PostManager, basename='posts')
urlpatterns = router.urls
