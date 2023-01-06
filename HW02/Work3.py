# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

num = int(input("Введите целое число (количество чисел последовательности и переменную n): "))
my_list = []
summ = 0
for i in range(1, num + 1):
    el = round(((1 + 1/i)**i), 2)
    my_list.append(el)
    summ += el
    print('{:05.2f}'.format(el))


print(my_list)
print(f"Сумма: {summ}")