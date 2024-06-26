"""
1) Подсчет суммы всех четных чисел от 1 до n. Реализовать двумя видами циклов
"""

print("Задание 1")
n = int(input("Введите n: "))  # Считает до n включительно

s = 0
for i in range(0, n + 1, 2):
    s += i
print(s)

s = 0
i = 0
while i <= n:
    s += i
    i += 2
print(s)

print()

"""
2) Найти самое длинное слово из массива. Реализовать двумя видами циклов
"""

print("Задание 2")
array = ["kldjfhkjfg", "jdhjdh", "jeshkfhfbdhjdb", "lsjd"]
m = ''
for ar in array:
    if len(ar) > len(m):
        m = ar
print(m)

m = ''
i = 0
while i < len(array):
    if len(array[i]) > len(m):
        m = array[i]
    i += 1
print(m)
print()

"""
3) Расчет факториала числа с выводом каждого шага.
"""

print("Задание 3")
n = int(input("Введите число: "))
f = 1
for i in range(1, n + 1):
    f *= i
    print(f)
print()

"""
4) Вывести каждый 3 элемент списка вместе с его индексом, используя enumerate()
"""

print("Задание 4")
enum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print("Список: ", enum)
for index, value in enumerate(enum):
    if (index + 1) % 3 == 0:
        print(index, value)
print()

"""
5) Напечатать таблицу умножения для числа n, использовать f строки
"""

print("Задание 5")
n = int(input())
for i in range(11):
    print(f'{i} * {n} = {i * n}')
print()

"""
6) Подсчитать количество цифр в числе. Реализовать двумя видами циклов
"""

print("Задание 6")
n = input("Введите число: ")
count = 0
for _ in n:
    count += 1
print(count)

count = 0
i = 0
while i < len(n):
    count += 1
    i += 1
print(count)
print()

"""
7) Проверить, является ли строка палиндромом (зеркальная)
"""

print("Задание 7")
s = input("Введите строку: ")
print("Строка: " + s)
if s[::-1] == s:
    print("Является палиндромом")
else:
    print("Не является палиндромом")
print()

"""
8) Определить, содержит ли список дубликаты
"""

print("Задание 8")
list = [1, 2, 2, 3, 4, 5, 12, 2]
print("Список ", list)
if len(list) == len(set(list)):
    print("Нет дубликатов")
else:
    print("Есть дубликаты")

print()

"""
9) Удалить все дубликаты из списка без использования дополнительных структур. 
    Реализовать двумя видами циклов, для удаления можно использовать pop() либо del
"""

print("Задание 9")
list9 = [12, 13, 14, 134, 12, 14, 12]
print("Исходный список: ", list9)
list9.sort()
for i in range(len(list9) - 1):
    if list9[i] == list9[i + 1]:
        list9[i] = ''

for i in range(len(list9)):
    for i, v in enumerate(list9):
        if v == '':
            list9.pop(i)

print(list9)

list9 = [12, 13, 14, 134, 12, 14, 12]
print("Исходный список: ", list9)
list9.sort()
i = 0
while i < len(list9) - 1:
    if list9[i] == list9[i + 1]:
        list9[i] = ''
    i += 1

i = 0
while i < len(list9):
    for ind, v in enumerate(list9):
        if v == '':
            list9.pop(ind)
    i += 1

print(list9)

print()

"""
10) Вывести каждую букву строки в обратном порядке без использования reversed() или [::-1]
"""

print("Задание 10")
n = input("Введите строку: ")
for i in range(len(n) - 1, -1, -1):
    print(n[i])
print()
