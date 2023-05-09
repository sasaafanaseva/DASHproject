
from django.db.models import F
from django.test import TestCase
from .models import Tasks
from .forms import TasksForm
from django.urls import reverse
import sqlite3

# Create your tests here.


class DummyTestCase(TestCase): #тесты на логику

    @classmethod
    def setUp(self):
        Tasks.objects.create(title='Арсений', boy_age=18, score=0, size='')
        Tasks.objects.create(title='Антон', boy_age=18, score=1, size='Уступил место')
        Tasks.objects.create(title='Александр', boy_age=18, score=3, size='Проводил')


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


class AuthorModelTest(TestCase): #тесты для моделей

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Tasks.objects.create(title='Арсений', boy_age=18, score=1, size='Открыл дверь')

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


class TasksFormTest(TestCase): #тесты для форм

    @classmethod
    def test_form_label(cls):
        form = TasksForm()
        assert form.fields['title'].label == 'ФИО'

    def test_form_arg(cls):
        form = TasksForm()
        assert form.fields['size'].label != 'Подарил цветы'


class TasksViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Create 13 authors for pagination tests
        Tasks.objects.create(title='Арсений', boy_age=18, score=6, size='Подвез до дома')
        Tasks.objects.create(title='Сема', boy_age=21, score=-4, size='Ответил "ок" на сообщение')

    def test_view_rating(self):
        resp = self.client.get(reverse('rating'))
        self.assertEqual(resp.status_code, 200)

    def test_view_home(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_create(self):
        resp = self.client.get(reverse('create'))
        self.assertEqual(resp.status_code, 200)
