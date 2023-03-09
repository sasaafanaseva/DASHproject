from django.shortcuts import render, redirect
from .models import Tasks
from .forms import TasksForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def index(request):
    tasks = Tasks.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'main/lk.html')


def signup(request):
    if request.method == "POST":
        # username = request.POST.get('username')
        username = request.POST['username']
        age = request.POST['age']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.username = username

        myuser.save()

        messages.success(request, "Ура ты новый пользователь приложения! Рады видеть тебя здесь")

        return redirect('signin')

    return render(request, 'main/signup.html')


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(usermane=username, password=pass1)

        if user is not None:
            login(request, user)
            username = user.usermane
            return render(request, "main/lk.html", {"username": username})

        else:
            messages.error(request, "Те тот пароль, иди вспоминай")
            return redirect("about")

    return render(request, 'main/signin.html')


def signout(request):
    logout(request)
    messages.success(request, "ты вышла из аккаунта")
    return redirect("home")


def create(request):
    error = ''
    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "введи нормально пжпж"

    form = TasksForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)
