from rest_framework import viewsets, mixins, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from cats import serializers, models

from users.models import Profile


class CatView(viewsets.ModelViewSet, mixins.DestroyModelMixin):
    queryset = models.Cat.objects.all()
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter, 
        filters.OrderingFilter,
    ]
    # search_fields = ['color', 'description', 'age']
    ordering_fields = '__all__'

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.CreateCatSerializer
        return serializers.CatSerializer

    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
    def perform_update(self, serializer):
        if self.request.user != serializer.owner:
            return Response(status=401)
        return super().perform_update(serializer)


class ReviewView(viewsets.ModelViewSet):
    serializer_class = serializers.ReviewSerializer
    queryset = models.Review.objects.all()
