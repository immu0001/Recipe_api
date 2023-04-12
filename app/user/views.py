"""
Views for the user API.

"""
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import (
    AuthTokenSerializer,
    UserSerializer
    )

class CreateUserView(generics.CreateAPIView):
    # generics.CreateAPIView handles HTTP post request thats designed for creating objects in the DB.
    """
    Create a new user in the System.
    """
    serializer_class = UserSerializer

class CreateTokenView(ObtainAuthToken):
    """Create a new Auth token for user."""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
