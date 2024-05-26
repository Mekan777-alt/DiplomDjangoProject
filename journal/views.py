from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from schedule.models import Subject, Schedule
from .models import Group, User, Grade
from django.views.decorators.http import require_POST
from django.contrib import messages


@login_required
def journal(request):
    groups = Group.objects.all().distinct()
    subjects = Subject.objects.all().distinct()

    selected_group_id = request.GET.get('group_id')
    selected_subject_id = request.GET.get('subject_id')
    selected_lesson_id = request.GET.get('lesson_id')

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
            lessons = Schedule.objects.filter(subject=selected_subject, group=selected_group)

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
    })


@login_required
@require_POST
def add_mark(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        subject_id = request.POST.get('subject_id')
        mark = request.POST.get('mark')
        subject_date_id = request.POST.get('lesson_id')
        print(subject_date_id)
        student = get_object_or_404(User, id=student_id)
        subject = get_object_or_404(Subject, id=subject_id)
        subject_date = get_object_or_404(Schedule, id=subject_date_id)

        teacher = request.user

        grade, created = Grade.objects.update_or_create(
            student=student,
            subject=subject,
            subject_date=subject_date,
            teacher=teacher,
            defaults={'mark': mark}
        )

        success_message = 'Оценка успешно добавлена.' if created else 'Оценка успешно обновлена.'
        messages.success(request, success_message)

        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    else:
        return HttpResponseBadRequest("Invalid request method")

