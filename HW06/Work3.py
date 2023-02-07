# Задача: предложить улучшения кода 
# c помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
# вывод неповторяющихся элементов списка. Использовано ENUMERATE
import random


def fill_list(list1, n):
    for _ in range(n):
        list1.append(random.randint(0, n // 2))


def single_nums(list1):
    new_list = []

    for i, el in enumerate(list1):
        flag = True

        for j in range(i):
            if el == list1[j]:
                flag = False
                break
        for j in range(i+1, len(list1)):
            if el == list1[j]:
                flag = False
                break
        if flag:
            new_list.append(el)
    return new_list

def main():
    num = 20  
    my_list = []
    fill_list(my_list, num)
    print(my_list)
    print(single_nums(my_list))

main()