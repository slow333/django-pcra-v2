from django.db import models
from django.contrib.auth.models import User

class SSHInfo(models.Model):
    login_id = models.CharField(max_length=20, null=False)
    ip_address = models.GenericIPAddressField(null=False)
    password = models.TextField(null=False)

    user = models.ManyToManyField(User)