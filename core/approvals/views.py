from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Approval
from .serializers import ApprovalSerializer


class ApprovalViewSet(viewsets.ModelViewSet):
    serializer_class = ApprovalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Approval.objects.all()

    def perform_create(self, serializer):
        serializer.save(approved_by=self.request.user)