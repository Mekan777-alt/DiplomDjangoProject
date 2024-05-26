from django.shortcuts import render
from schedule.models import Schedule
from django.contrib.auth.decorators import login_required


@login_required
def schedule_view(request):
    schedule_data = {}
    groups = Schedule.objects.values_list('group__name', flat=True).distinct()
    days_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    day_names = dict(Schedule.DAYS_OF_WEEK)

    for group in groups:
        group_schedule = Schedule.objects.filter(group__name=group).order_by('day_of_week', 'number')
        schedule_data[group] = {}
        for day in days_of_week:
            schedule_data[group][day] = group_schedule.filter(day_of_week=day)

    context = {
        'schedule_data': schedule_data,
        'day_names': day_names,
    }

    return render(request, 'schedule/schedule.html', context)


@login_required
def session_schedule_view(request):
    schedule_data = {}
    groups = Schedule.objects.filter(type_schedule__schedule_type='Сессия').values_list('group__name', flat=True).distinct()
    days_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    day_names = dict(Schedule.DAYS_OF_WEEK)

    for group in groups:
        group_schedule = Schedule.objects.filter(group__name=group, type_schedule__schedule_type='Сессия').order_by('day_of_week', 'number')
        schedule_data[group] = {}
        for day in days_of_week:
            schedule_data[group][day] = group_schedule.filter(day_of_week=day)

    context = {
        'session_schedule': Schedule.objects.filter(type_schedule__schedule_type='Сессия'),
        'schedule_data': schedule_data,
        'day_names': day_names,
    }

    return render(request, 'schedule/session_schedule.html', context)