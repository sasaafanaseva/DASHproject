from django.contrib.auth.models import User
from django.db.models import F
from django.test import TestCase
from .models import Tasks, BoyGirlMatch
from .forms import TasksForm, ReviewForm
from django.urls import reverse
import sqlite3
# Create your tests here.


class DummyTestCase(TestCase): #тесты на логику

    @classmethod
    def setUp(self):
        first_boy = Tasks.objects.create(title='Арсений', boy_age=18, score=0, size='')
        second_boy = Tasks.objects.create(title='Антон', boy_age=18, score=1, size='Уступил место')
        third_boy = Tasks.objects.create(title='Александр', boy_age=18, score=3, size='Проводил')
        girl = User.objects.create(username='Dasha') #представим, что всех парней добавляет Даша
        BoyGirlMatch.objects.create(boy=first_boy, girl=girl)
        BoyGirlMatch.objects.create(boy=second_boy, girl=girl)
        BoyGirlMatch.objects.create(boy=third_boy, girl=girl, dash="закреп")


    def test_make_base_postupki(self): #подключение к sql
        connection = sqlite3.connect('sqlite_python.db')
        cursor = connection.cursor()
        cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='lala' ''')
        result = cursor.fetchone()[0]
        assert result == 0
        cursor.execute(
            """CREATE TABLE lala(
                move text,
                score int);
            """)
        connection.commit()
        cursor.execute("""
                              INSERT INTO lala(move, score) VALUES
                                  ('Уступил место', 1),
                                  ('Обнял при встрече', 2),
                                  ('Проводил', 3),
                                  ('Принес кофе', 4);
                           """)
        connection.commit()
        cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='lala' ''')
        result = cursor.fetchone()[0]
        assert result == 1
        cursor.execute(
            """DROP TABLE lala;"""
        )
        connection.commit()
        cursor.close()

    def test_a(self): #получение баллов по поступку
        with sqlite3.connect('sqlite_python.db') as connection:
            cursor = connection.cursor()
            cursor.execute(f"""SELECT score FROM postupok WHERE move = 'Принес кофе';""")
            ball = int(cursor.fetchall()[0][0])  # получаем балл за поступок
        assert ball == 4

    def test_bil_takoi_paren(self): #проверка на существование парня в базе и обновление его баллов
        paren = 'Антон'
        is_present = Tasks.objects.filter(title=paren).exists()
        self.assertTrue(is_present == 1)
        postupok = str(Tasks.objects.get(title=paren).size + ' ' + 'Принес кофе')
        Tasks.objects.filter(title=paren).update(score=F("score") + 4, size = postupok)
        self.assertTrue('Уступил место Принес кофе', Tasks.objects.get(title=paren).size)
        self.assertTrue(5, Tasks.objects.get(title=paren).score)

    def test_nov_paren(self): #проверка на существование парня в базе и его добавление
        paren = 'Кирилл'
        is_present = Tasks.objects.filter(title=paren).exists()
        self.assertTrue(is_present == 0)
        Tasks.objects.create(title=paren, boy_age=18, score=0, size='')
        self.assertTrue('Кирилл', Tasks.objects.get(id=4))

    def create_my_boy(self): #связь таблиц, когда девочка закрепляет своего парня и только своего
        girl = User.objects.get(username='Dasha')
        parni = BoyGirlMatch.objects.filter(girl=girl)
        for i in parni:
            if i.dash == "закреп":
                self.assertEquals('Александр', i.boy.title)
                BoyGirlMatch.objects.get(girl=girl, boy=i).update(dash='пока не решила')
        parni = BoyGirlMatch.objects.filter(girl=girl)
        dash = 0
        for i in parni:
            if i.dash == "закреп":
                dash = 1
        self.assertEquals(dash, 0)


class AuthorModelTest(TestCase): #тесты для моделей

    @classmethod
    def setUpTestData(cls):
        boy = Tasks.objects.create(title='Арсений', boy_age=18, score=1, size='Открыл дверь')
        girl = User.objects.create(username='Dasha')
        BoyGirlMatch.objects.create(boy=boy, girl=girl, dash="закреп")

    def test_title_label(self):
        author=Tasks.objects.get(id=1)
        self.assertEquals(str(author),'Арсений')

    def test_score_label(self):
        author=Tasks.objects.get(id=1)
        field_label = author._meta.get_field('score').verbose_name
        self.assertEquals(field_label, '10')

    def test_max_length(self):
        author=Tasks.objects.get(id=1)
        max_length = author._meta.get_field('title').max_length
        self.assertEquals(max_length, 50)

    def test_object_name(self):
        author = Tasks.objects.get(id=1)
        expected_object_name = author.title
        self.assertEquals(expected_object_name, str(author))

    def test_match(self):
        match = BoyGirlMatch.objects.get(id=1).boy
        self.assertEquals(str(match), "Арсений")

    def test_match_def(self):
        match = BoyGirlMatch.objects.get(id=1)
        default_value = match._meta.get_field('dash').default
        self.assertEquals(default_value, "пока не решила")


class TasksFormTest(TestCase): #тесты для форм

    @classmethod
    def test_form_label(cls):
        form = TasksForm()
        assert form.fields['title'].label == 'ФИО'

    def test_form_arg(cls):
        form = TasksForm()
        assert form.fields['size'].label != 'Подарил цветы'

    def test_form_comments(cls):
        form = ReviewForm()
        cls.assertEquals(form.fields['text'].label, 'Если оценок стало мало')


class TasksViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Tasks.objects.create(title='Арсений', boy_age=18, score=6, size='Подвез до дома')
        Tasks.objects.create(title='Сема', boy_age=21, score=-4, size='Ответил "ок" на сообщение')

    def test_view_rating(self):
        resp = self.client.get(reverse('rating'))
        self.assertEqual(resp.status_code, 200)

    def test_view_home(self):
        resp = self.client.get(reverse('signin'))
        self.assertEqual(resp.status_code, 200)
