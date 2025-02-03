from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm, BuyerRegistrationForm
from .models import *

# python manage.py runserver

# users = [{'username': 'vasya', 'password': 'qw1qw1qw1', 'age': 21},
#          {'username': 'petya', 'password': 'petya12345', 'age': 24},
#          {'username': 'kolya', 'password': 'kolya12345', 'age': 40}]

def anchor(request):
    return render(request, 'anchor.html')

def main_page(request):
    title = 'Домик у Озера'
    description = 'Домик у Озера. C видом на счастье...'
    context = {
        'title': title,
        'description': description,

    }
    return render(request, 'lakehouse.html', context)

def book(request):
    title = 'Забронировать'
    description = 'Забронировать'
    # buttons = ['Домик у Озера', 'Баня', 'Лодка']
    games = Game.objects.all()
    context = {
        'title': title,
        'description': description,
        'games': games,


    }
    return render(request, 'book.html', context)

def info(request):
    title = 'Информация о Домике у Озера'
    description = 'Позвольте вам рассказать о нашем Домике у Озера...'
    photo_summer = 'images/lakehouse_summer.jpg'
    photo_winter = 'images/lakehouse_winter.jpg'
    context = {
        'title': title,
        'description': description,
        'photo_summer': photo_summer,
        'photo_winter': photo_winter,

    }
    return render(request, 'info.html', context)

def menu(request):
    return render(request, 'menu.html')


def sign_up_by_html(request):
    if request.method == 'POST':
        # получаем данные
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_repeat = request.POST.get('password_repeat')
        age = request.POST.get('age')

        info = {'username': username,
                'age': age,

                }

        user_exists = any(user['username'] == username for user in users)

        if user_exists:
            info['error'] = "Такой пользователь уже существует"
        elif password != password_repeat:
            info['error'] = "Пароли не совпадают"
        elif int(age) < 18:
            info['error'] = "Вам нет 18 лет"
        else:
            # Если ошибок нет, добавляем пользователя в список
            users.append({'username': username, 'password': password, 'age': int(age)})
            return HttpResponse(f"Приветствуем, {username}!")
        return render(request, 'fifth_task/registration_page.html', info)
    # если это метод GET
    return render(request, 'fifth_task/registration_page.html')


def sign_up_by_django(request):
    if request.method == 'POST':
        form = BuyerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем нового покупателя в БД
            return redirect('success_page')  # Перенаправляем на страницу успеха

    else:
        form = BuyerRegistrationForm()
    return render(request, 'registration_page_django.html', {'form': form})

def success_page(request):
    return render(request, 'successful_registration.html')