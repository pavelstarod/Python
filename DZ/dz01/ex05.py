# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


x = int(input('введите X = '))
y = int(input('введите Y = '))
z = int(input('введите Z = '))
print()
print(f'¬(X ⋁ Y ⋁ Z)' ' = ' '¬X ⋀ ¬Y ⋀ ¬Z')
a = not (x or y or z)
b = not (x) and not (y) and not (z)
print()
print(f'¬(X ⋁ Y ⋁ Z) = {a}')
print(f'¬X ⋀ ¬Y ⋀ ¬Z = {b}')
print()
print('Вывод:')
if (a == b):
    print(True)
else:
    print(False)
