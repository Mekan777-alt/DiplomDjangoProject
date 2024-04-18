from django import forms
from authentication.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _


class UserCreationForm(forms.Form):
    first_name = forms.CharField(label='first_name', min_length=5, max_length=150)
    last_name = forms.CharField(label='last_name', min_length=5, max_length=150)
    email = forms.EmailField(label='email')
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

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
        user = User.objects.create_user(
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password1'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
        )
        return user
