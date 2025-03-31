from django.contrib import admin
from identity.models.identity_model import IdentityModel


@admin.register(IdentityModel)
class IdentityAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "username",
    )
    