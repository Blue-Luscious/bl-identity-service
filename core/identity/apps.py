from django.apps import AppConfig


class IdentityConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "identity"
    verbose_name = "Gestion de Identidades"


    def ready(self) -> None:
        
        from identity.models import (
            identity_model,      
        )
        
        from identity.admins import (
            identity_admin,
        )
    