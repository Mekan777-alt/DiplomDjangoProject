from django.shortcuts import render
from authentication.models import User


def grading_view(request):
    students = User.objects.filter()
    if request.method == 'POST':
        form = GradingForm(request.POST)
        if form.is_valid():
            # Process the grades here
            pass
    else:
        form = GradingForm()
    return render(request, 'grading.html', {'students': students, 'form': form})
