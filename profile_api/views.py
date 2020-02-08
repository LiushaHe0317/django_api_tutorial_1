from rest_framework import viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from . import serializers, models, permissions


class UserProfileViewset(viewsets.ModelViewSet):
    """handle creating and updating user profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.UpdateOwnProfile]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'email']


class UserLoginAPIView(ObtainAuthToken):
    """handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

