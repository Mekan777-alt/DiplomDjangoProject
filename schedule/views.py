from django.shortcuts import render
from schedule.models import Schedule
from authentication.enum import Groups
from django.contrib.auth.decorators import login_required


@login_required
def schedule(request):

    if request.user.role == Groups.STUDENT.name:
        group = request.user.student_group

        schedule_data = {group.name: Schedule.objects.filter(group=group)}

        days_of_week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']

        return render(request, 'schedule/schedule.html', {'schedule_data': schedule_data, 'days_of_week': days_of_week})

    else:
        return render(request, 'auth/login.html')
