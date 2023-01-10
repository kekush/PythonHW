# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

dec_number = int(input("Введите число в десятичной системе исчисления: "))
num_list = []
binary_num_list = []

while dec_number != 0:
    binary_num_list.append(dec_number % 2)
    dec_number = int(dec_number/2)
print("Ваше число в двоичной системе исчисления = ", end='')
for i in reversed(range(len(binary_num_list))):
    print(binary_num_list[i], end='')

#или
# a = int(input('Введите число: '))
# print(bin(a))