from django.core.mail import send_mail
from django.db.backends import sqlite3
from django.shortcuts import render, redirect
from .models import Tasks
from .forms import TasksForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import logging
import sqlite3
global mydict
from django.db.models import F

# from ..taskmanager import settings


#from urod.taskmanager.taskmanager import settings

## вставлено сашей

def boy_exists(paren): #проверка на существование парня в базе
    is_present = Tasks.objects.filter(title=paren).exists()
    if is_present:
        return True
    return False

## нормальное продолжение полины


def index(request):
    tasks = Tasks.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'main/lk.html')


def signup(request):
    if request.method == "POST":
        # username = request.POST.get('username')
        username = request.POST['username']
        fname = request.POST['fname']
        age = request.POST['age']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist")
            return redirect('about')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered")
            return redirect('about')

        if len(username) > 10:
            messages.error(request, "Username must be under 10 charcters")
            return redirect('about')

        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched")
            return redirect('about')

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric")
            return redirect('about')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.save()
        messages.success(request, "Ура ты новый пользователь приложения! Рады видеть тебя здесь")

        # # Welcome Email
        #
        # subject = "Welcome to DASH"
        # message = "Привет" + myuser.first_name + ".Добро пожаловать в наше приложение"
        # from_email = settings.EMAIL_HOST_USER
        # to_list = [myuser.email]
        # send_mail(subject, message, from_email, to_list, fail_silently=True)

        return redirect('signin')

    return render(request, 'main/signup.html')


def signin(request):
    if request.method == "POST": #вход в аккаунт
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(usermane=username, password=pass1)

        if user is not None: #если правильно вошли в аккаунт
            login(request, user)
            fname = user.first_name
            return render(request, "main/lk.html", {'fname': fname})

        else:
            messages.error(request, "Те тот пароль, иди вспоминай")
            return redirect('about')

    return render(request, "main/signin.html")


def signout(request): #выход из аккаунта
    logout(request)
    messages.success(request, "ты вышла из аккаунта")
    return redirect('home')

def create(request): #создание парня
    error = ''
    if request.method == 'POST':
        form = TasksForm(request.POST) #имя парня и поступок лежат в переменной form
        if form.is_valid():
            with sqlite3.connect('sqlite_python.db') as connection:
                cursor = connection.cursor()
                cursor.execute(f"""select score from postupok WHERE move = '{form.data['size']}';""")
                ball = int(cursor.fetchall()[0][0]) #получаем балл за поступок
            if boy_exists(form.data['title']):
                postupok = str(Tasks.objects.get(title=form.data['title']).size) + "\n" + form.data['size']
                Tasks.objects.filter(title=form.data['title']).update(score=F("score") + ball, size = postupok)
                messages.success(request, "твой парень уже есть в базе, ему добавлен новый поступок")
            else:
                Tasks.objects.create(title = form.data['title'], boy_age = form.data['boy_age'], score = ball, size = form.data['size'])
                messages.success(request, "ты его единственная, парень добавлен в базу")
            return redirect('home')
        else:
            error = "введи нормально пжпж"

    form = TasksForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)
