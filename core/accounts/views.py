from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Profile
from .serializers import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.profile.role == 'admin':
            return Profile.objects.all()
        return Profile.objects.filter(user=user)