# Generated by Django 4.2 on 2023-06-15 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boygirlmatch',
            name='dash',
            field=models.TextField(choices=[('закреп', 'закреп'), ('пока не решила', 'пока не решила')], default='пока не решила'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='size',
            field=models.TextField(choices=[('Открыл дверь', 'Открыл дверь -- 1'), ('Помог расчесать волосы', 'Помог расчесать волосы -- 1'), ('Сделал комплимент', 'Сделал комплимент -- 1'), ('Уступил место', 'Уступил место -- 2'), ('Обнял при встрече', 'Обнял при встрече -- 2'), ('Помог донести тяжелую сумку', 'Помог донести тяжелую сумку -- 2'), ('Взял за руку', 'Взял за руку -- 3'), ('Выложил твой пост в сторис', 'Выложил твой пост в сторис -- 3'), ('Накинул свою куртку в холодный вечер', 'Накинул свою куртку в холодный вечер -- 3'), ('Помог убраться', 'Помог убраться -- 3'), ('Проводил', 'Проводил -- 3'), ('Подарил цветы', 'Подарил цветы -- 4'), ('Принес кофе', 'Принес кофе -- 4'), ('Помыл посуду', 'Помыл посуду -- 4'), ('Встретил после учебы', 'Встретил после учебы -- 4'), ('Смотрел со мной беременна в 16', 'Смотрел со мной беременна в 16 -- 4'), ('Рассказал смешную шутку', 'Рассказал смешную шутку -- 4'), ('Починил нерабочий код', 'Починил нерабочий код -- 5'), ('Помог с чем-то', 'Помог с чем-то -- 5'), ('Поддержал и выслушал', 'Поддержал и выслушал -- 5'), ('Подарил плюшевую игрушку', 'Подарил плюшевую игрушку -- 5'), ('Подвез до дома', 'Подвез до дома -- 6'), ('Познакомил с друзьями', 'Познакомил с друзьями -- 6'), ('Скинул дз', 'Скинул дз -- 6'), ('Потанцевал со мной', 'Потанцевал со мной -- 6'), ('Пригласил погулять', 'Пригласил погулять -- 6'), ('Красиво сфотографировал', 'Красиво сфотографировал -- 7'), ('Отдал свою футболку/толстовку', 'Отдал свою футболку/толстовку -- 7'), ('Познакомил с родителями', 'Познакомил с родителями -- 7'), ('Понес на руках', 'Понес на руках -- 7'), ('Подарил духи', 'Подарил духи -- 7'), ('Приготовил ужин', 'Приготовил ужин -- 8'), ('Заступился за меня', 'Заступился за меня -- 8'), ('Сделал массаж', 'Сделал массаж -- 8'), ('Сходил со мной за одеждой', 'Сходил со мной за одеждой -- 8'), ('Оплатил маникюр', 'Оплатил маникюр -- 8'), ('Подарил украшение', 'Подарил украшение -- 8'), ('Достал билеты на концерт любимой группы', 'Достал билеты на концерт любимой группы --8'), ('Поцеловал', 'Поцеловал -- 9'), ('Признался в любви', 'Признался в любви -- 9'), ('Обнял и лежал с тобой', 'Обнял и лежал с тобой -- 9'), ('Внимательно слушал тебя', 'Внимательно слушал тебя -- 9'), ('Устроил романтическое свидание', 'Устроил романтическое свидание -- 10'), ('Подарил путешествие', 'Подарил путешествие -- 10'), ('Приехал неожиданно из другой страны', 'Приехал неожиданно из другой страны -- 10'), ('Поменторил проект', 'Поменторил проект -- 10'), ('Включил Егора Крида', 'Включил Егора Крида -- 10'), ('Поставил клоуна', 'Поставил клоуна -- -2'), ('Разбудил', 'Разбудил -- -3'), ('Разозлил', 'Разозлил -- -3'), ('Не проявил интерес', 'Не проявил интерес -- -4'), ('ответил "ок" на сообщение', 'ответил "ок" на сообщение -- -4'), ('Обманул, но признался сам', 'Обманул, но признался сам -- -4'), ('Критиковал мой образ', 'Критиковал мой образ -- -4'), ('Устроил в квартире срач', 'Устроил в квартире срач -- -4'), ('Не помог', 'Не помог -- -4'), ('Не подождал', 'Не подождал -- -4'), ('Сравнил с бывшими девушками', 'Сравнил с бывшими девушками -- -4'), ('Ответил "ок" на сообщение', 'Ответил "ок" на сообщение -- -2'), ('Забуллил', 'Забуллил -- -5'), ('Некрасиво пошутил', 'Некрасиво пошутил -- -5'), ('Забыл забрать тебя', 'Забыл забрать тебя -- -5'), ('Сильно напился', 'Сильно напился -- -5'), ('Не пошел со мной в зал', 'Не пошел со мной в зал -- -5'), ('Поставил свое желание выше моего', 'Поставил свое желание выше моего -- -5'), ('Не хочет знакомить с родителями', 'Не хочет знакомить с родителями -- -5'), ('Уверенно нёс ересь', 'Уверенно нёс ересь -- -5'), ('Флиртовал с другой', 'Флиртовал с другой -- -6'), ('Накричал', 'Накричал -- -6'), ('Опоздал на встречу', 'Опоздал на встречу -- -6'), ('Не понял намек', 'Не понял намек -- -6'), ('Не разговаривал со мной весь вечер', 'Не разговаривал со мной весь вечер -- -6'), ('Ушел на тусовку не предупредив', 'Ушел на тусовку не предупредив -6'), ('Попросил счет пополам', 'Попросил счет пополам -- -6'), ('Отстранился при друзьях', 'Отстранился при друзьях -- -6'), ('Сказал что мое хобби бесполезно', 'Сказал что мое хобби бесполезно -- -6'), ('Не поздравил с днем рождения', 'Не поздравил с днем рождения -- -6'), ('Не захотел разрешить конфликт', 'Не захотел разрешить конфликт -- -7'), ('Жаловался на жизнь', 'Жаловался на жизнь -- -7'), ('Плохо относится к твоим друзьям', 'Плохо относится к твоим друзьям -- -7'), ('Жёстко контролил', 'Жёстко контролил -- -7'), ('Сказал <= чем друзья', 'Сказал <= чем друзья -- 7'), ('Обманул и увиливал', 'Обманул и увиливал -- -7'), ('Нарушил личные границы', 'Нарушил личные границы -- -8'), ('Попросил изменить мою внешность', 'Попросил изменить мою внешность -- -8'), ('Не выполнил обещание', 'Не выполнил обещание -- -8'), ('Сказал что он всегда прав', 'Сказал что он всегда прав -- -8'), ('Общался с бывшей', 'Общался с бывшей -8'), ('Манипулировал', 'Манипулировал -- -8'), ('Не захотел проводить время вдвоем', 'Не захотел проводить время вдвоем -- -8'), ('Обвинил меня в своих неудачах', 'Обвинил меня в своих неудачах -- -8'), ('Слился со свидания', 'Слился со свидания -- -8'), ('Довел до слез', 'Довел до слез -- -9'), ('Игнорировал', 'Игнорировал -- -9'), ('Бросил', 'Бросил -- -10'), ('Изменил', 'Изменил -- -10')], default='Ничего не сделал'),
        ),
    ]
