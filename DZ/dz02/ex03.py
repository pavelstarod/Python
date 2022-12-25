# Реализуйте алгоритм перемешивания списка.
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
# максимум использование библиотеки Random для получения случайного int
from random import randint

list = []
l = int(input('Введите длину списка: '))
for i in range(l):
    list.append(i)
print(list)

new_list = []
while len(new_list) < l:
    x = randint(0, len(list)-1)
    if x not in new_list:
        new_list.append(x)
print(new_list)
