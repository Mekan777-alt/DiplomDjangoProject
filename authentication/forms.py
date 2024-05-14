from django import forms
from authentication.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from authentication.models import Group
from django.shortcuts import get_object_or_404


class UserCreationForm(forms.Form):
    first_name = forms.CharField(label='Имя', min_length=5, max_length=150)
    last_name = forms.CharField(label='Фамилия', min_length=5, max_length=150)
    email = forms.EmailField(label='Электронная почта')
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput)
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=False, label='Группа')

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if len(password1) < 8:
            raise ValidationError(_("Пароль слишком короткий. Он должен содержать как минимум 8 символов."))
        if password1.isdigit():
            raise ValidationError(_("Пароль не должен состоять только из цифр."))
        if password1.lower() in ['password', '123456', 'qwerty']:
            raise ValidationError(_("Пароль слишком распространенный. Выберите более сложный пароль."))
        return password1

    def save(self, commit=True):
        group_name = self.cleaned_data['group']
        group = Group.objects.get(name=group_name)
        user = User.objects.create_user(
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password1'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            student_group=group,
            role='STUDENT'
        )
        return user
