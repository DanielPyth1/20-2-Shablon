from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.core.mail import send_mail
from django.conf import settings
from .forms import RegisterForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.tokens import default_token_generator
from django.utils.crypto import get_random_string
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
import secrets

User = get_user_model()

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        token = secrets.token_hex(16)
        user.token = token
        user.save()

        verification_link = f"http://{self.request.get_host()}/users/verify-email/{token}/"
        send_mail(
            'Подтвердите свою регистрацию',
            f'Спасибо за регистрацию! Пожалуйста, перейдите по ссылке для подтверждения: {verification_link}',
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )
        return redirect('email_verification_sent')

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

def password_reset_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()

        if user:
            new_password = get_random_string(8)
            user.password = make_password(new_password)
            user.save()

            send_mail(
                'Восстановление пароля',
                f'Ваш новый пароль: {new_password}',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
            return redirect('login')

    return render(request, 'registration/password_reset.html')

def verify_email(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.token = ''
    user.save()
    return redirect('login')
