from django.urls import path
from .views import RegisterView, password_reset_view, verify_email
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('password-reset/', password_reset_view, name='password_reset'),
    path('verify-email/<str:token>/', verify_email, name='verify_email'),
]
