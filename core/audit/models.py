from django.db import models
from django.contrib.auth.models import User
from operations.models import Operation


class AuditLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='audit_logs')
    action = models.CharField(max_length=255)
    related_operation = models.ForeignKey(
        Operation, on_delete=models.SET_NULL, null=True, blank=True, related_name='audit_logs'
    )
    details = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action} by {self.user} at {self.timestamp}"