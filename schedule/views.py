from django.shortcuts import render
from schedule.models import Schedule, Session
from django.contrib.auth.decorators import login_required


@login_required
def schedule_view(request):
    schedule_data = {}
    groups = Schedule.objects.filter(type_schedule__schedule_type='Предмет').values_list('group__name', flat=True).distinct()
    days_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    day_names = dict(Schedule.DAYS_OF_WEEK)

    for group in groups:
        group_schedule = Schedule.objects.filter(group__name=group, type_schedule__schedule_type='Предмет').order_by('day_of_week', 'number')
        schedule_data[group] = {day: [] for day in days_of_week}
        for schedule in group_schedule:
            schedule_data[group][schedule.day_of_week.lower()].append({
                'number': schedule.number,
                'time_from': schedule.time_from,
                'time_to': schedule.time_to,
                'subject': schedule.subject,
                'type_of_lesson': schedule.type_of_lesson,
                'teacher': schedule.teacher.get_full_name() if schedule.teacher else 'N/A',
                'place_of_performance': schedule.place_of_perfomance,
            })

    active_day = request.GET.get('day')
    if not active_day:
        active_day = days_of_week[0]
    active_schedules = {group: schedules.get(active_day, []) for group, schedules in schedule_data.items()}

    context = {
        'schedule_data': schedule_data,
        'day_names': day_names,
        'active_day': active_day,
        'active_schedules': active_schedules,
    }

    return render(request, 'schedule/schedule.html', context)



@login_required
def session_schedule_view(request):
    day_names = dict(Session.TYPE_CHOICES)
    selected_semester = request.GET.get('semester', next(iter(day_names)))

    session_schedule = Schedule.objects.filter(type_schedule__schedule_type='Сессия', session_number=selected_semester)

    context = {
        'session_schedule': session_schedule,
        'day_names': day_names,
        'selected_semester': selected_semester,
    }

    return render(request, 'schedule/session_schedule.html', context)



