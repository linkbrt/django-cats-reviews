from rest_framework import viewsets

from cats import serializers, models

class CatView(viewsets.ModelViewSet):
    serializer_class = serializers.CatSerializer
    queryset = models.Cat.objects.all()

