from rest_framework import decorators, viewsets, mixins
from rest_framework.permissions import AllowAny

from .serializers import CreateProfileSerializer


@decorators.permission_classes((AllowAny,))
class UserView(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = CreateProfileSerializer
