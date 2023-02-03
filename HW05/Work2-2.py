# Создайте программу для игры с конфетами
# Добавьте игру против бота    


import random

conf = 2021 
step = 28  
move = step + 1 

print(f'ВСЕГО КОНФЕТ: {conf}. МОЖНО ВЗЯТЬ НЕБОЛЬШЕ {step} КОНФЕТ. ИГРА НАЧАЛАСЬ!')
player = random.randint(1, 2)
if player == 2:
    num = conf % move
    print(f'Берет компьютер: {num}')
    player = 1
    conf -= num
else:
    num = int(input('Возьми конфеты: '))
    while num < 1 or num > step or num > conf:
        if num > conf:
            print(f'Осталось только {conf} конфеты!')
        else:
            print(f'Вы можете взять не более {step} конфет! Осталось конфет: {conf}')
        num = int(input('Возьми конфеты: '))
    conf -= num
    num = conf % move
    if not num:  
        num = random.randint(1, step)
        print(f'Берет компьютер: {num}')
    else:
        print(f'Берет компьютер: {num}')
    conf -= num


while conf > 0:
    print('Осталось конфет: ', conf)

    if player == 2:
        num = move - num
        print(f'Берет компьютер: {num}')
        player = 1
    else:
        num = int(input('Возьми конфеты: '))
        while num < 1 or num > step or num > conf:
            if num > conf:
                print(f'Осталось только {conf} конфеты!')
            else:
                print(f'Вы можете взять не более {step} конфет! Осталось конфет: {conf}')
            num = int(input('Возьми конфеты: '))
        player = 2
    conf -= num

if player == 2:
    print('Ты победил!')
else:
    print('Победил компьютер!')