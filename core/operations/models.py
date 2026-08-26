from django.db import models
from django.contrib.auth.models import User
from devices.models import Device


class Operation(models.Model):
    OPERATION_TYPE_CHOICES = [
        ('dry_run', 'Dry Run'),
        ('write', 'Write'),
        ('rollback', 'Rollback'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('executed', 'Executed'),
        ('rolled_back', 'Rolled Back'),
    ]

    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='operations')
    command = models.TextField()
    operation_type = models.CharField(max_length=20, choices=OPERATION_TYPE_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='operations')
    created_at = models.DateTimeField(auto_now_add=True)
    executed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.operation_type} on {self.device.name} ({self.status})"