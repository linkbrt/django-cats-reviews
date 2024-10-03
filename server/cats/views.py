from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins

from cats import serializers, models

from users.models import Profile


class CatView(viewsets.ModelViewSet, mixins.DestroyModelMixin):
    serializer_class = serializers.CatSerializer
    queryset = models.Cat.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
    def perform_update(self, serializer):
        # if self.request.user != serializer.user:
        #     return Response(status=401)
        return super().perform_update(serializer)


class ReviewView(viewsets.ModelViewSet):
    serializer_class = serializers.ReviewSerializer
    queryset = models.Review.objects.all()
