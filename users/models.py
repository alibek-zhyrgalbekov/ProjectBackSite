from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class ConfirmationCode(models.Model):
    code = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    valid_until = models.DateTimeField(null=True)