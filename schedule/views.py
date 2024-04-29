from django.shortcuts import render
from schedule.models import Group, Schedule


def schedule(request):

    groups = Group.objects.all()

    schedule_data = {}

    for group in groups:

        schedule_data[group.name] = Schedule.objects.filter(group=group)

    return render(request, 'schedule/schedule.html', {'schedule_data': schedule_data})
