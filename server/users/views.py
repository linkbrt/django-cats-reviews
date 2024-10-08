from rest_framework import decorators, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .serializers import CreateProfileSerializer
from .models import Profile


@decorators.api_view(("POST",))
@decorators.permission_classes([AllowAny])
def create_user(request):
    serializer = CreateProfileSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    Profile.objects.create_user(**serializer.data)

    return Response(status=status.HTTP_201_CREATED)
