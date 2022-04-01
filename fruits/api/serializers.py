from rest_framework import serializers

from fruits.models import Fruit, Region

class FruitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fruit
        fields = ('id', 'name', 'region')

class RegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Region
        fields = ('id', 'name')
