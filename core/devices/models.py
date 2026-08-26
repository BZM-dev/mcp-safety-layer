from django.db import models

class Device(models.Model):
    DEVICE_TYPE_CHOICES = [
        ('router', 'Router'),
        ('switch', 'Switch'),
        ('firewall', 'Firewall'),
        ('access_point', 'Access Point'),
        ('other', 'Other'),
    ]

    VENDOR_CHOICES = [
        ('cisco', 'Cisco'),
        ('juniper', 'Juniper'),
        ('mikrotik', 'MikroTik'),
        ('huawei', 'Huawei'),
        ('other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('unreachable', 'Unreachable'),
    ]

    name = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField()
    device_type = models.CharField(max_length=20, choices=DEVICE_TYPE_CHOICES)
    vendor = models.CharField(max_length=20, choices=VENDOR_CHOICES)
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    


