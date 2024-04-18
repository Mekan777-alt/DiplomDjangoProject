from django.urls import path
from django.contrib.auth import views as auth_views
from authentication import views

app_name = 'authentication'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
