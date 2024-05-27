from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from authentication.forms import UserCreationForm
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.db import IntegrityError
from authentication.enum import Groups


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Регистрация прошла успешно. Теперь вы можете войти!')
                return JsonResponse({'success': True})
            except IntegrityError as e:
                return JsonResponse({'success': False, 'error': "Электронная почта уже зарегистрирована."})
        else:
            return JsonResponse({'success': False, 'error': 'Ошибка при регистрации. Пожалуйста, исправьте ошибки в форме.'})
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            if user.role == Groups.TEACHER.name:
                return redirect(reverse('journal:journal'))
            else:
                return redirect(reverse('schedule:schedule'))
        else:
            messages.error(request, "Неверный адрес электронной почты или пароль")
    return render(request, 'auth/login.html')
