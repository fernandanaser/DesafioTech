from rest_framework import viewsets
from desafioapp.api import serializers
from desafioapp import models


class RegionViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RegionSerializer
    queryset = models.Region.objects.all()


class FruitViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FruitSerializer
    queryset = models.Fruit.objects.all()
