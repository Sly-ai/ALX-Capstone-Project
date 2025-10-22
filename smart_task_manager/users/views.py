from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import User
from .serializers import UserSerializer, UserCreateSerializer
from .permissions import IsSuperUser

# Create your views here.
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSuperUser]  # Only superuser can list/create users

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserCreateSerializer
        return UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # Users can view/update their own, superuser all

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE']:
            return [IsSuperUser()]
        return super().get_permissions()

    def get_object(self):
        obj = super().get_object()
        if not self.request.user.is_superuser and obj != self.request.user:
            raise PermissionDenied("You do not have permission to access this user.")
        return obj