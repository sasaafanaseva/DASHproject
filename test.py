import click
import csv
import os

global mydict


def paren_v_base(name):
    with open('parni.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['name'] == name:
                csvfile.close()
                return True
        csvfile.close()
        return False


def hochy_parnia(paren, age, ball, postupok): #по name определяем есть ли такой парень в базе, далее либо запусаем полное добавление, либо обновление баллов
    r = paren_v_base(paren)
    if r == True:
        print("ваш парень есть в базе и мы добавили ему", ball, "баллов")
        dobav_ballov(paren, age, ball, postupok)
    else:
        print("вы его единственная, ваш парень добавлен в базу")
        dobav_parnia(paren, age, ball, postupok)


def dobav_parnia(paren, age, ball, postupok): #полное добавление парня
    with open('parni.csv', 'a', newline='') as csvfile:
        fieldnames = ['name', 'age', 'ball', 'move']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if os.stat('parni.csv').st_size == 0:
            writer.writeheader()
        writer.writerow({'name': paren, 'age': age, 'ball': ball, 'move': postupok})
    csvfile.close()



def dobav_ballov(paren, age, ball, postupok): #если парень существует, то обновим его баллы (перезапишем весь файл)
    with open('parni.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        with open('new0.csv', 'w', newline='') as file:
            fieldnames = ['name', 'age', 'ball', 'move']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for row in reader:
                if row['name'] != paren:
                    writer.writerow({'name': row['name'], 'age': row['age'], 'ball': row['ball'], 'move': row['move']})
                else:
                    new_ball = int(row['ball']) + ball
                    new_postupok = postupok + "и " + row['move']
                    writer.writerow({'name': paren, 'age': age, 'ball': new_ball, 'move': new_postupok})
    file.close()
    csvfile.close()
    with open('new0.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        with open('parni.csv', 'w', newline='') as file:
            fieldnames = ['name', 'age', 'ball', 'move']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for row in reader:
                writer.writerow({'name': row['name'], 'age': row['age'], 'ball': row['ball'], 'move': row['move']})
    file.close()
    csvfile.close()

def filter_po_age(znach):
    with open('parni.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if int(row['age']) == int(znach):
                print(row['name'], row['age'], row['ball'], row['move'])
    csvfile.close()

def filter_po_ball(znach):
    with open('parni.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if int(row['ball']) >= int(znach):
                print(row['name'], row['age'], row['ball'], row['move'])
    csvfile.close()



@click.command()
@click.argument("name", nargs=2, type=str)
# nargs отвечает за кол-во аргументов, которые мы забираем из командной строки - попадают как кортеж
# при nargs = -1 : required - означает что хотя бы один аргумент должен передаться
#type - тип передаваемого аргумента из командной строки

@click.option("--age", "-a", default=18, help="возраст парня")

@click.option("--ball", "-b", default=0, help="баллы парня")
# --ball - вызывает считывание из командной сторки,
# "ball" - переменная куда все это сохраняется
# defalt=0 - подставляет в качестве изначального значения int, благодаря чему теперь дефолтно будет передаваться не строка, а число,
# help - что будет написано в справке

@click.argument("move", nargs=-1, type=str)

def hello(name, age, ball, move): #функция вызывающая другие
    paren = name[0] + " " + name[1]
    postupok = ""
    for i in move:
        postupok += i
        postupok += " "
    #print(paren, " ", age, " ", ball, " ", postupok)
    if paren == "filter parney":
        if move[0] == "age":
            filter_po_age(move[1])
        if move[0] == "ball":
            filter_po_ball(move[1])
    else:
        hochy_parnia(paren, age, ball, postupok)
    #dobav_parnia(paren, age, ball, postupok)


if __name__ == '__main__':
    hello()

