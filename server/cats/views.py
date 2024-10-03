from rest_framework import viewsets, mixins, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from cats import serializers, models

from users.models import Profile


class CatView(viewsets.ModelViewSet, mixins.DestroyModelMixin):
    queryset = models.Cat.objects.all()
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]
    filterset_fields = ['breed']
    ordering_fields = "__all__"

    def get_serializer_class(self):
        if self.request.method == "GET":
            return serializers.CatSerializer
        return serializers.CreateCatSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if self.request.user != instance.owner:
            return Response(status=401)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if self.request.user != instance.owner:
            return Response(status=401)
        return super().destroy(request, *args, **kwargs)


class ReviewView(viewsets.ModelViewSet):
    serializer_class = serializers.ReviewSerializer
    queryset = models.Review.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if self.request.user != instance.owner:
            return Response(status=401)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if self.request.user != instance.owner:
            return Response(status=401)
        return super().destroy(request, *args, **kwargs)


class BreedView(viewsets.ModelViewSet):
    serializer_class = serializers.BreedSerializer
    queryset = models.Breed.objects.all()
