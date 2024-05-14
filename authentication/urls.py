from django.urls import path
from django.contrib.auth import views as auth_views
from authentication import views

app_name = 'authentication'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('password_resset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_resset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
]
