from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from schedule.models import Subject, Schedule, ScheduleType
from .models import Group, User, Grade
from django.views.decorators.http import require_POST
from django.contrib import messages


@login_required
def journal(request):
    current_user = request.user

    groups = Group.objects.filter(schedule__teacher=current_user).distinct()
    subjects = Subject.objects.filter(schedule__teacher=current_user).distinct()
    schedule_types = ScheduleType.objects.all()

    selected_group_id = request.GET.get('group_id')
    selected_subject_id = request.GET.get('subject_id')
    selected_grade_type = request.GET.get('grade_type')

    selected_group = None
    selected_subject = None
    selected_lesson = None
    students = []
    lessons = []

    if selected_group_id:
        selected_group = get_object_or_404(Group, id=selected_group_id)
        students = User.objects.filter(student_group=selected_group)

        if selected_subject_id:
            selected_subject = get_object_or_404(Subject, id=selected_subject_id)

            if selected_grade_type:
                lessons = Schedule.objects.filter(subject=selected_subject, group=selected_group,
                                                  type_schedule__schedule_type=selected_grade_type)

            selected_lesson_id = request.GET.get('lesson_id')

            if selected_lesson_id:
                selected_lesson = get_object_or_404(Schedule, id=selected_lesson_id)

    return render(request, 'journal/journal.html', {
        'groups': groups,
        'students': students,
        'subjects': subjects,
        'lessons': lessons,
        'selected_group': selected_group,
        'selected_subject': selected_subject,
        'selected_lesson': selected_lesson,
        'selected_grade_type': selected_grade_type,
        'schedule_types': schedule_types
    })


@login_required
@require_POST
def add_mark(request):
    subject_id = request.POST.get('subject_id')
    lesson_id = request.POST.get('lesson_id')
    grade_type = request.POST.get('grade_type')  # Получаем тип расписания
    subject = get_object_or_404(Subject, id=subject_id)
    lesson = get_object_or_404(Schedule, id=lesson_id)
    teacher = request.user

    for key, value in request.POST.items():
        if key.startswith('student_id_'):
            student_id = value
            mark_key = 'mark_' + student_id
            mark = request.POST.get(mark_key)

            if mark:
                student = get_object_or_404(User, id=student_id)
                grade, created = Grade.objects.update_or_create(
                    student=student,
                    subject=subject,
                    subject_date=lesson,
                    teacher=teacher,
                    defaults={'mark': mark, 'grade_type': grade_type}
                )

    messages.success(request, 'Оценки успешно добавлены/обновлены.')
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
