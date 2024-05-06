from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.contrib import messages
from authentication.forms import UserCreationForm
from django.urls import reverse
from django.contrib.auth import authenticate, login


def register(request):
    group = Group.objects.all()
    form = UserCreationForm()
    context = {
        'form': form,
        'group': group
    }
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация прошла успешно. Теперь вы можете войти!')
            return redirect(reverse('authentication:login'))
        else:
            messages.error(request, 'Ошибка при регистрации. Пожалуйста, исправьте ошибки в форме.')
            return render(request, 'auth/register.html', context)
    else:
        return render(request, 'auth/register.html', context)


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('schedule:schedule')
        else:
            messages.error(request, "Неверный адрес электронной почты или пароль")
    return render(request, 'auth/login.html')
