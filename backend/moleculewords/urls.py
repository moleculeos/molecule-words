from rest_framework.routers import SimpleRouter
from .views import WordViewSet, LanguageViewSet


router = SimpleRouter()
router.register(r'languages', LanguageViewSet)
router.register(r'words', WordViewSet, basename="words")

urlpatterns = router.urls