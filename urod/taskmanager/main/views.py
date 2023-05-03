from .forms import LoginForm
from django.core.mail import send_mail
from django.db.backends import sqlite3
from django.shortcuts import render, redirect
from .models import Tasks
from .forms import TasksForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import logging
import sqlite3
global mydict

from taskmanager import settings


## вставлено сашей

def boy_exists(paren): #проверка на существование парня в базе
    with sqlite3.connect('sqlite_python.db') as connection:
        cursor = connection.cursor()
        cursor.execute("""SELECT us_name FROM main_tasks""")
        df = cursor.fetchall()
        for i in df:
            if i[0] == paren:
                return True
        return False

def add_ball(paren, ball, postupok):  # если парень существует, то обновим его балл
    with sqlite3.connect('sqlite_python.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f"""SELECT move FROM main_tasks WHERE us_name = '{paren}';""")
        pos = cursor.fetchall()[0]
        post = str(pos)[2:-3] + ', ' + postupok
        cursor.execute(f"""UPDATE main_tasks SET score = score + {ball}, move = '{post}' WHERE us_name = '{paren}';""")
        connection.commit()

## нормальное продолжение полины


def index(request):
    tasks = Tasks.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'main/lk.html')


def home(request):
    return render(request, "main/lk.html")


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('home')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('home')

        if len(username) > 20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('home')

        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('home')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        # myuser.is_active = False
        myuser.save()
        messages.success(request, "Ты новый пользователь приложения DASH!")
        user = authenticate(username=username, password=pass1)
        login(request, user)
        return redirect('home')

    return render(request, "main/signup.html")


def signin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], pass1=cd['pass1'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    messages.error(request, 'Your account is disabled')
                    return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'home')




    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #
    #     user = authenticate(username=username, password=password)
    #     if user:
    #         login(request, user)
    #         return redirect('home')
    #     else:
    #         messages.error(request, 'Your account is disabled')
    #         return redirect('home')
    # else:
    #     return render(request, "main/signin.html")

        # username = request.POST['username']
        # pass1 = request.POST['pass1']
        #
        # user = authenticate(username=username, password=pass1)
        # login(request, user)
        # fname = user.first_name
        # return render(request, "main/lk.html", {"fname": fname})

        # if user is not None:
        #     login(request, user)
        #     fname = user.first_name
        #     # messages.success(request, "Logged In Sucessfully!!")
        #     return render(request, "main/lk.html", {"fname": fname})
        # else:
        #     messages.error(request, "idi nahui")
        #     return redirect('signin')

    # return render(request, "main/signin.html")


def signout(request):
    logout(request)
    messages.success(request, "дам пока пока")
    return redirect('home')


def create(request): #создание парня
    error = ''
    if request.method == 'POST':
        form = TasksForm(request.POST) #имя парня и поступок лежат в переменной form
        if form.is_valid():
            if boy_exists(form.title):
                add_ball(form.title, form.score, form.task)
                return redirect('home')
            else:
                form.save()
                return redirect('home')
                # my_boy(form.title, form.boy_age, form.score, form.task)
            # form.save()
            # return redirect('home')
        else:
            error = "введи нормально пжпж"

    form = TasksForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)
