from django import forms
from .models import Grade
from authentication.models import User, Group
from schedule.models import Subject


class GradeForm(forms.ModelForm):
    def __init__(self, *args, user=None, **kwargs):
        super(GradeForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['student'].queryset = User.objects.filter(student_group=user.subject.group)

    class Meta:
        model = Grade
        fields = ['student', 'lesson', 'score']


class GroupSelectionForm(forms.Form):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), label='Группа')
    subject = forms.ModelChoiceField(queryset=Subject.objects.all(), label='Предмет')
