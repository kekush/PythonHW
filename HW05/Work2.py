# Создайте программу для игры с конфетами человек против человека.
import random

conf = 2021
step = 28
# num = conf + 1
player = random.randint(1, 2)
while conf > 0:
    print('Осталось конфет: ', conf)
    
    if player == 1:
        player = 2
    else:
        player = 1
    num = int(input(f'Ход у {player}-ого игрока: '))
    while num < 1 or num > step or num > conf:
        if num > conf:
            print(f'Осталось только {conf} конфеты!')
        else:
            print(f'Вы можете взять не более {step} конфет! Осталось конфет: {conf}')
        num = int(input(f'Ход у {player}-ого игрока: '))
    else:
        conf -= num

print('Победил: ', player)