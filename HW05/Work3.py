# 3. Создайте программу для игры в "Крестики-нолики".

import random


def field(my_list):
    print('   | X1| X2| X3|')
    print('----------------')
    for i in 0, 1, 2:
        print(f'Y{i + 1} |', end='')
        for j in 0, 1, 2:
            print(f' {my_list[i][j]} |', end='') 
        print()
        print('----------------')


def answer(label):
    print(f'ВЫИГРАЛИ {label}!')
    return False


def check(label, my_list):
    for i in 0, 1, 2:
        if my_list[0][i] == label and my_list[1][i] == label and my_list[2][i] == label:
            return answer(label)
        elif my_list[i][0] == label and my_list[i][1] == label and my_list[i][2] == label:
            return answer(label)
    else:
        if my_list[0][0] == label and my_list[1][1] == label and my_list[2][2] == label:
            return answer(label)
        elif my_list[2][0] == label and my_list[1][1] == label and my_list[0][2] == label:
            return answer(label)
        else:
            return True


play = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
field(play)

player = random.randint(1, 2)
counter = 0
flag = True
while flag:
    if player == 2:
        x = random.randint(1, 3)
        y = random.randint(1, 3)
        if play[y-1][x-1] == ' ':
            print(f'Ход Бота: x = {x}, y = {y}')
            play[y-1][x-1] = '0'
            flag = check('0', play)
            counter += 1
            player = 1
            field(play)
    else:
        print('Твой ход:')
        x = int(input('Введите х: '))
        while 1 > x or x > 3:
            x = int(input('Введите верное значение х: '))
        y = int(input('Введите y: '))
        while 1 > y or y > 3:
            y = int(input('Введите верное значение y: '))
        # player = 2
        if play[y-1][x-1] != ' ':
            print('Поле уже занято')
        else:
            play[y-1][x-1] = 'x'
            flag = check('x', play)
            counter += 1
            player = 2
            field(play)
    if counter == 9 and flag:
        print('ХОДОВ НЕ ОСТАЛОСЬ!')
        flag = False