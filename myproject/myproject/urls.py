from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from users.views import RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('register/', RegisterView.as_view(), name='register'),
    path('users/', include('users.urls')),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', lambda request: HttpResponseRedirect('catalog/')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
