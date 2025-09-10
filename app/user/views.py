"""
views for the user api
"""

from rest_framework import generics# , permissions

from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """ create a new user in the system"""
    serializer_class = UserSerializer
   # permission_classes = (permissions.AllowAny)