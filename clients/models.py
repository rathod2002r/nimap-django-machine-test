from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    client_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='clients_created')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.client_name

