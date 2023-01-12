# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19


import random

my_list = []
l = int(input('Введите длинну списка: '))
for item in range(l):
    amount = random.randint(0, 3)
    number = round(random.uniform(0, 10), amount)
    if number == int(number):
        my_list.append(int(number))
    else:
        my_list.append(number)
print(my_list)

my_list2 = []
for item in range(len(my_list)):
    if my_list[item] % 1 != 0:
        my_list2.append(my_list[item])

my_list3 = []
for item in range(len(my_list2)):
    my_list3.append(round(my_list2[item] % 1, 3))

print(
    f'Вывод разницы max и min дробной части: {round(max(my_list3)-min(my_list3), 3)}')
