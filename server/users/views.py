from users.models import Profile

from rest_framework import status, decorators, viewsets, mixins
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .serializers import CreateProfileSerializer


@decorators.permission_classes((AllowAny,))
class CreateUserView(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = CreateProfileSerializer
