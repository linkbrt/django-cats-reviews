from rest_framework import viewsets

from cats import serializers, models

class CatView(viewsets.ModelViewSet):
    serializer_class = serializers.CatSerializer
    queryset = models.Cat.objects.all()


class ReviewView(viewsets.ModelViewSet):
    serializer_class = serializers.ReviewSerializer
    queryset = models.Review.objects.all()
