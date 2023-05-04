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

def create_base():
    try:
        connection = sqlite3.connect('sqlite_python.db')
        cursor = connection.cursor()
        print("База данных создана и успешно подключена к SQLite")
        cursor.execute(
            """CREATE TABLE postupok(
                move text,
                score int);
            """)
        connection.commit()
        cursor.execute("""
                          INSERT INTO postupok(move, score) VALUES
                          ('Открыл дверь', 1),
                          ('Помог расчесать волосы', 1),
                          ('Сделал комплимент', 1),
                          ('Уступил место', 2),
                          ('Обнял при встрече', 2),
                          ('Помог донести тяжелую сумку', 2),
                          ('Взял за руку', 3),
                          ('Выложил твой пост в сторис', 3),
                          ('Накинул свою куртку в холодный вечер', 3),
                          ('Помог убраться', 3),
                          ('Проводил', 3),
                          ('Подарил цветы', 4),
                          ('Принес кофе', 4),
                          ('Встретил после учебы', 4),
                          ('Починил нерабочий код', 5),
                          ('Помог с чем-то', 5),
                          ('Поддержал и выслушал', 5),
                          ('Подарил плюшевую игрушку', 5),
                          ('Подвез до дома', 6),
                          ('Познакомил с друзьями', 6),
                          ('Скинул дз', 6),
                          ('Потанцевал со мной', 6),
                          ('Пригласил погулять', 6),
                          ('Красиво сфотографировал', 7),
                          ('Отдал свою футболку/толстовку', 7),
                          ('Познакомил с родителями', 7),
                          ('Рассказал смешную шутку', 4),
                          ('Понес на руках', 7),
                          ('Подарил духи', 7),
                          ('Приготовил ужин', 8),
                          ('Заступился за меня', 8),
                          ('Сделал массаж', 8),
                          ('Сходил со мной за одеждой', 8),
                          ('Оплатил маникюр', 8),
                          ('Подарил украшение', 8),
                          ('Достал билеты на концерт любимой группы', 8),
                          ('Поцеловал', 9),
                          ('Признался в любви', 9),
                          ('Обнял и лежал с тобой', 9),
                          ('Внимательно слушал тебя', 9),
                          ('Устроил романтическое свидание', 10),
                          ('Подарил путешествие', 10),
                          ('Разбудил', -3),
                          ('Разозлил', -3),
                          ('Не проявил интерес', -4),
                          ('Обманул, но признался сам', -4),
                          ('Критиковал мой образ', -4),
                          ('Устроил в квартире срач', -4),
                          ('Не помог', -4),
                          ('Не подождал', -4),
                          ('Сравнил с бывшими девушками', -4),
                          ('Забуллил', -5),
                          ('Некрасиво пошутил', -5),
                          ('Забыл забрать тебя', -5),
                          ('Сильно напился', -5),
                          ('Не пошел со мной в зал', -5),
                          ('Поставил свое желание выше моего', -5),
                          ('Не хочет знакомить с родителями', -5),
                          ('Флиртовал с другой', -6),
                          ('Накричал', -6),
                          ('Опоздал на встречу', -6),
                          ('Не понял намек', -6),
                          ('Не разговаривал со мной весь вечер', -6),
                          ('Ушел на тусовку не предупредив', -6),
                          ('Попросил счет пополам', -6),
                          ('Отстранился при друзьях', -6),
                          ('Сказал что мое хобби бесполезно', -6),
                          ('Не поздравил с днем рождения', -6),
                          ('Не захотел разрешить конфликт', -7),
                          ('Жаловался на жизнь', -7),
                          ('Плохо относится к твоим друзьям', -7),
                          ('Жёстко контролил', -7),
                          ('Обманул и увиливал', -7),
                          ('Нарушил личные границы', -8),
                          ('Попросил изменить мою внешность', -8),
                          ('Не выполнил обещание', -8),
                          ('Сказал что он всегда прав', -8),
                          ('Общался с бывшей', -8),
                          ('Манипулировал', -8),
                          ('Не захотел проводить время вдвоем', -8),
                          ('Обвинил меня в своих неудачах', -8),
                          ('Слился со свидания', -8),
                          ('Довел до слез', -9),
                          ('Игнорировал', -9),
                          ('Бросил', -10),
                          ('Изменил', -10);
                        """)
        connection.commit()
        # cursor.execute("""select * from po""")
        # tables = cursor.fetchall()
        # print(tables)
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)

    finally:
        if (connection):
            connection.close()
            print("Соединение с SQLite закрыто")

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
    create_base()
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
