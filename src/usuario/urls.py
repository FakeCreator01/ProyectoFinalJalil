from django.urls import path, include
from .views import Login, LogoutView, Signup

app_name = 'usuario'

urlpatterns = [
    path("login/", Login.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("signup/", Signup.as_view(), name="signup")
]
