from django.contrib import admin

# Register your models here.
from users.models import ConfirmationCode

admin.site.register(ConfirmationCode)