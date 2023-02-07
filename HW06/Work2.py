# Задача: предложить улучшения кода 
# c помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

num = int(input('Введите число: '))

def f(x):
    mult = 1
    for i in range(1, x + 1):
        mult *= i
    return mult


list2 = [el for el in range(1, num+1)]
print(list2)
list2 = list(map(f, list2))
print(list2)