# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. tr54

my_list = [1, 2, 3, 5, 9, 5, 3, 10, 2, 4]

result_list = []
for i in my_list:
    if my_list.count(i) == 1:
        result_list.append(i)
print(result_list)