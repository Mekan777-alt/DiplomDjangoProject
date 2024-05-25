from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from .forms import GradeForm, GroupSelectionForm
from schedule.models import Group, Schedule
from journal.models import Grade
from authentication.models import User


@method_decorator(login_required, name='dispatch')
class JournalView(View):
    template_name = 'journal/journal.html'

    def get(self, request):
        teaching_assignment_form = GroupSelectionForm()
        grade_form = GradeForm(user=request.user)
        return render(request, self.template_name, {
            'teaching_assignment_form': teaching_assignment_form,
            'grade_form': grade_form,
        })

    def post(self, request):
        teaching_assignment_form = GroupSelectionForm(request.POST)
        grade_form = GradeForm(request.POST, user=request.user)

        if 'teaching_assignment_submit' in request.POST and teaching_assignment_form.is_valid():
            teaching_assignment_form.save()
            messages.success(request, 'Назначение успешно сохранено')
            return redirect('journal:journal')

        if 'group_submit' in request.POST and teaching_assignment_form.is_valid():
            selected_group = teaching_assignment_form.cleaned_data['group']
            selected_subject = teaching_assignment_form.cleaned_data['subject']
            students = User.objects.filter(student_group=selected_group, role='STUDENT')
            lessons = Schedule.objects.filter(group=selected_group, subject=selected_subject)
            grade_form = GradeForm(user=request.user)
            grade_form.fields['student'].queryset = students
            grade_form.fields['lesson'].queryset = lessons

            return render(request, self.template_name, {
                'teaching_assignment_form': teaching_assignment_form,
                'grade_form': grade_form,
                'students': students,
                'lessons': lessons,
            })

        if 'grade_submit' in request.POST and grade_form.is_valid():
            grade_form.save()
            messages.success(request, 'Оценка успешно сохранена')
            return redirect('journal:journal')

        return render(request, self.template_name, {
            'teaching_assignment_form': teaching_assignment_form,
            'grade_form': grade_form,
        })
