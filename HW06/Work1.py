# Задача: предложить улучшения кода 
# c помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

def summa1(num):
    summa = 0
    for el in num:
        if el.isdigit():
            summa += int(el)
    print('Сумма цифр числа =', summa)

def my_func(func, x):
    func(x)

def summa2(list1):
    summa = 0
    for el in list1:
        summa += el
    return summa

num = '12.3'
print('Передача функции аргументом другой функции:')
my_func(summa1, num)
print()

print('Используем List Comprehension:')
my_list = [int(el) for el in num if el.isdigit()]
print(my_list)
print(f'Сумма цифр числа = {summa2(my_list)}')