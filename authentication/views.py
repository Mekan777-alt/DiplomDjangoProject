from django.shortcuts import render, redirect
from django.contrib import messages
from authentication.forms import UserCreationForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация прошла успешно. Теперь вы можете войти!')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка при регистрации. Пожалуйста, исправьте ошибки в форме.')
            return render(request, 'auth/register.html', {"form": form})
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})
