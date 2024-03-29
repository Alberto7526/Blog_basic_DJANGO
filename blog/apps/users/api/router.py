from django.urls import path
from apps.users.api.views import RegisterView, UserView

# para la autenticación por token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("auth/register", RegisterView.as_view()),
    path("auth/login", TokenObtainPairView.as_view()),
    path("auth/token/refresh", TokenRefreshView.as_view()),
    path("auth/me", UserView.as_view()),
]
