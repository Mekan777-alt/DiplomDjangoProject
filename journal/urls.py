from django.urls import path
from . import views

app_name = 'journal'

urlpatterns = [
    path('journal/', views.journal, name='journal'),
    path('add_mark/', views.add_mark, name='add_mark'),
    path('view_grades/', views.grades_view, name='view_grades'),
]