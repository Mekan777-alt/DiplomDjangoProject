from django.urls import path
from schedule import views

app_name = 'schedule'

urlpatterns = [
    path('schedule/', views.schedule_view, name='schedule'),
]
