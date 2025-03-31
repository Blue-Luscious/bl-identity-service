from django.contrib.auth.models import AbstractUser 
from django.db import models


class IdentityModel(AbstractUser):
    
    """
    Identity Model.

    Abstract User Fields:
        username (str): Username.
        first_name (str): First name.
        last_name (str): Last name.
        email (str): Email.
        is_staff (bool): Is staff User.
        is_active (bool) Is active User.
        date_joined (DateTime): Joined date.
    """

    class Meta:
        verbose_name = "Identidad"
        verbose_name_plural = "Identidades"
