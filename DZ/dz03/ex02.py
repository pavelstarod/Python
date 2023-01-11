# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

my_list = input('vvedite: ').split()
my_list2 = []
my_list3 = []

for item in range(len(my_list)):
    my_list2.append(int(my_list[item]))
print(my_list2)

for item in range(len(my_list2)):
    if item < len(my_list2)//2:
        my_list3.append(my_list2[item]*my_list2[item*(-1)-1])
    elif len(my_list2) % 2 == 1 and item == (len(my_list2)//2):
        my_list3.append(my_list2[item]**2)

print(my_list3)
