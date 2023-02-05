import random
import os
from datetime import date
import time
import copy

kon = {'Торт': ['мука, масло, варенье', 200, 7],
       'Маффин': ['тесто, шоколад', 50, 23],
       'Пирожное': ['слоеное тесто, крем', 60, 31]}

col_clientov = 0
vyrochka = 0


def document(chek):
    try:
        os.mkdir(f'{date.today()}')
    except:
        pass
    os.chdir(f'{date.today()}')
    q = random.randint(1, 1000)
    try:
        f = open(f'Chek № {col_clientov + 1}.txt', 'w', encoding='utf-8')
        for i, j in chek.items():
            f.write(f'{i} {j} \n')
    except:
        pass
    os.chdir('..')


def prodaga(kon):
    chek = {}
    global prod
    prod = copy.deepcopy(kon)
    s = 0
    while True:
        a = input(
            "Введите название продукта,если хотите завершить покупку отправьте n: ").capitalize()
        if a not in kon or a == 'n':
            break
        f = int(input("Введите колличество: "))
        if f > kon[a][2]:
            print('У нас не достаточно данного товара ')
            continue
        s += f * kon[a][1]
        kon[a][2] -= f
        chek[a] = [f'Колличество {f}', f'Цена {f * kon[a][1]}']
    chek['Итоговая цена: '] = s
    return chek


def pay(kon, cash):
    global vyrochka
    global col_clientov
    chek = prodaga(kon)
    if cash >= chek['Итоговая цена: ']:
        document(chek)
        cash -= chek['Итоговая цена: ']
        col_clientov += 1
        vyrochka += chek['Итоговая цена: ']
    else:
        print('У вас недостаточно средств')
        kon = copy.deepcopy(prod)

    return kon, cash


def pocupatel(kon):
    cash = random.randint(0, 1000)
    while True:
        print(f'Колличество денег {cash}')
        b = int(input(''' 1 - Название – описание;
                          2 - Название – цена;
                          3 - Название – количество;
                          4 - Вся информация; 
                          5 - Приступить к покупке; 
                          6 - Выход; 
                          Введите число запроса: '''))
        for i, j in kon.items():
            if b == 1:
                print(i, j[0], sep=' - ')
            elif b == 2:
                print(i, j[1], sep=' - ')
            elif b == 3:
                print(i, j[2], sep=' - ')
            elif b == 4:
                print(i, j[0], j[1], j[2], sep=' - ')
            elif b == 5:
                cash = pay(kon, cash)[1]
                break

        if b == 6:
            break


def postavshchick(kon):
    s = int(input('Сколько наименований товара вы привезли? '))
    i = 0
    while i < s:
        a = input('Введите наименование товара: ').capitalize()
        b = int(input('Введите колличество товараа: '))
        if a in kon:
            kon[a][2] += b
        else:
            print('У нас нет такого наименования ')
            continue
        i += 1
    return kon


def administrator(kon):
    s = int(input(''' 1 - Выручка;
                      2 - Клиенты;
                      3 - Добавить товар;
                      4 - Удаление товара; 
                      5 - Изменение цены;
                      Введите действие: '''))
    if s == 1:
        print(vyrochka)
    elif s == 2:
        print(col_clientov)
    elif s == 3:
        d = input('Введите наименование товара ').capitalize()
        f = int(input('Введите колличество '))
        a = input('Введите состав ').lower()
        g = int(input('Введите цену '))
        kon[d] = [a, g, f]
    elif s == 4:
        a = input('Какое наименование вы хотите удалить? ').capitalize()
        del kon[a]
    elif s == 5:
        d = input('На какой товар вы хотите изменить стоимость? ').capitalize()
        s = int(input('Введите стоимость '))
        kon[d][1] = s
    return kon


def main(kon):
    a = int(input('''1 - Поставщик;
2 - Администратор;
3 - Покупатель;
Введите вашу роль: '''))
    if a == 1:
        postavshchick(kon)
    elif a == 2:
        administrator(kon)
    elif a == 3:
        pocupatel(kon)


max_time = 28800
start_time = time.time()
while (time.time() - start_time) < max_time:
    main(kon)
