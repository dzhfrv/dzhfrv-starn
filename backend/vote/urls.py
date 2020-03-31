from rest_framework.routers import SimpleRouter

from .views import VoteManager

router = SimpleRouter()
router.register('votes', VoteManager, basename='posts')
urlpatterns = router.urls
