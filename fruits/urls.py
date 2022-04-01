from django.urls import include, path
from rest_framework import routers
from .api.viewsets import FruitViewSet, RegionViewSet

router = routers.DefaultRouter()
router.register('fruits', FruitViewSet)
router.register('regions', RegionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

