from django.db import models

class STKPushDaraja(models.Model):
    merchant_request_id = models.CharField(max_length=120)
    checkout_request_id = models.CharField(max_length=120)
    response_code = models.CharField(max_length=120)
    response_description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
