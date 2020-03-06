from rest_framework import routers
from .api import GroceriesViewSet

router = routers.DefaultRouter()
router.register('api/groceries', GroceriesViewSet, 'groceries')

urlpatterns = router.urls