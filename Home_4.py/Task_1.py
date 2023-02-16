'''Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах. 
Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
m - кол-во элементов второго множества. 
Затем пользователь вводит сами элементы множеств.'''

import os

os.system("cls")

# n = int(input('Введите длину множества n: '))
# m = int(input('Введите длину множества m: '))

# set_n = set()
# for i in range(n):
#     n_1 = int(input())
#     set_n.add(n_1)
# print(set_n)

# set_m = set()
# for i in range(m):
#     m_1 = int(input())
#     set_m.add(m_1)
# print(set_m)

# list_1 = list(set_n.intersection(set_m))
# list_1.sort()
# print(*list_1)


# n = int(input('Введите длину множества n: '))
# m = int(input('Введите длину множества m: '))

# def make_set(a):
#     set_a = []
#     for i in range(a):
#         a_1 = int(input())
#         set_a.append(a_1)
#     return set(set_a)

# set_n = make_set(n)
# set_m = make_set(m)

# list_1 = list(set_n.intersection(set_m))
# list_1.sort()
# print(*list_1)



n, m = input().split()
first = {int(i) for i in input().split()}
second = {int(j) for j in input().split()}

print(type(second))

print(sorted(first.intersection(second)))
