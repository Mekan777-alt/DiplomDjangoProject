from django.urls import path
from schedule import views

app_name = 'schedule'

urlpatterns = [
    path('schedule/', views.schedule_view, name='schedule'),
    path('session_schedule/', views.session_schedule_view, name='session_schedule_view'),
]
