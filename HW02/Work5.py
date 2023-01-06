# Реализуйте алгоритм перемешивания списка.

from random import sample
my_list = [ 1, 2, 3, 4, 5, 6, 7]
shuffled_list = []
indexes = []

indexes = sample(range(0, len(my_list)), len(my_list))
print(indexes)

for i in range(len(my_list)):
    shuffled_list.append(my_list[indexes[i]])
print(shuffled_list)