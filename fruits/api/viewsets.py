from rest_framework import viewsets
from .serializers import FruitSerializer, RegionSerializer
from fruits.models import Fruit, Region

class FruitViewSet(viewsets.ModelViewSet):
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
