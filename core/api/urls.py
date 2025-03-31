from django.urls import path
from api.v1.views.login_api_view import LoginView
from api.v1.views.register_api_view import RegisterView

VERSION_PREFIX = "v1"

urlpatterns = [
    path(f"{VERSION_PREFIX}/login", LoginView.as_view(), name="login"),
    path(f"{VERSION_PREFIX}/register", RegisterView.as_view(), name="register"),
]
