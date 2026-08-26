from django.db import models
from django.contrib.auth.models import User
from devices.models import Device
from operations.models import Operation


class Approval(models.Model):
    DECISION_CHOICES = [
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    operation = models.ForeignKey(Operation, on_delete=models.CASCADE, related_name='approvals')
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='approvals')
    decision = models.CharField(max_length=10, choices=DECISION_CHOICES)
    comment = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.decision} by {self.approved_by} on {self.operation}"