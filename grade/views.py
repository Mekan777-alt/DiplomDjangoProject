from django.shortcuts import render
from authentication.models import User, Group

from django.shortcuts import render, redirect
from .models import Group, Student, Grade
from .forms import GradeForm


def grade_view(request):
    groups = Group.objects.all()
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grade_view')
    else:
        form = GradeForm()

    return render(request, 'grades/grade_view.html', {'form': form, 'groups': groups})

