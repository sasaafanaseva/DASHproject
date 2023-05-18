import click
import logging
global mydict
import sqlite3

#эти тесты помогут проверить логику программы при добавлении нового парня.
#можно через командную строку добавить своего мальчика

def create_base():
    try:
        connection = sqlite3.connect('sqlite_python.db')
        cursor = connection.cursor()
        cursor.execute(
            """CREATE TABLE postupok(
                move text,
                score int);
            """)
        connection.commit()
        cursor.execute(
            """CREATE TABLE boys(
                id integer PRIMARY KEY,
                us_name varchar(50) NOT NULL,
                age smallint,
                score int,
                move text);
            """)
        connection.commit()
        cursor.execute("""
                          INSERT INTO postupok(move, score) VALUES
                          ('Ничего не сделал', 0),
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
        cursor.close()

    except sqlite3.Error as error:
        logging.basicConfig(filename='app.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')
        logging.error("Ошибка при подключении к sqlite", error)

    finally:
        if (connection):
            connection.close()
            logging.basicConfig(level=logging.INFO, filename='app.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')
            logging.info('Соединение с SQLite закрыто')

def boy_exists(paren):
    cursor = connection.cursor()
    cursor.execute("""SELECT us_name FROM boys""")
    df = cursor.fetchall()
    for i in df:
        if i[0] == paren:
            return True
    return False

def my_boy(paren, age, ball, postupok):  #по name определяем есть ли такой парень в базе, далее либо запусаем полное добавление, либо обновление баллов
    r = boy_exists(paren)
    if r == True:
        logging.basicConfig(level=logging.INFO, filename='app.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')
        logging.info('your boyfriend is in the database and we added points to him')
        add_ball(paren, ball, postupok)
    else:
        logging.basicConfig(level=logging.INFO, filename='app.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')
        logging.info('you are his only one and your boyfriend has been added to the database')
        new_boy(paren, age, ball, postupok)

def new_boy(paren, age, ball, postupok):
    cursor = connection.cursor()
    cursor.execute(f"""
                    INSERT INTO boys(us_name, age, score, move) VALUES
                        ('{paren}', {age}, {ball}, '{postupok}');
                    """)
    connection.commit()

def add_ball(paren, ball, postupok):
    cursor = connection.cursor()
    cursor.execute(f"""select move from boys WHERE us_name = '{paren}';""")
    pos = cursor.fetchall()[0]
    post = str(pos)[2:-3] + ' ' + postupok
    cursor.execute(f"""UPDATE boys SET score = score + {ball}, move = '{post}' WHERE us_name = '{paren}';""")
    connection.commit()

@click.command()
@click.argument("name", nargs=2, type=str)
@click.option("--age", "-a", default=18, help="возраст парня")
@click.argument("move", nargs=-1, type=str)
def main(name, age, move):
    curs = connection.cursor()
    curs.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='postupok' ''')
    result = curs.fetchone()[0]
    # if result == 0:
    #     create_base()
    curs.close()
    error = ''
    paren = name[0] + " " + name[1]
    postupok = ""
    for i in move:
        postupok += i
        postupok += " "
    postupok = postupok[0:-1]
    cursor = connection.cursor()
    cursor.execute(f"""select score from postupok WHERE move = '{postupok}';""")
    ball = cursor.fetchall()[0][0]
    cursor.close()
    logging.basicConfig(level=logging.INFO, filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
    logging.info('Boy being processed')
    my_boy(paren, age, ball, postupok)

if __name__ == '__main__':
    with sqlite3.connect('sqlite_python.db') as connection:
        main()
