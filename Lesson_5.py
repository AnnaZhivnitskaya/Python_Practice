# Фибоначчи
# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ...,
# где # a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи

'''def fib(n):
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)
    
print(fib(7))'''


# Хакер Василий получил доступ к классному
# журналу и хочет заменить все свои минимальные
# оценки на максимальные. Напишите программу,
# которая заменяет оценки Василия,
# но наоборот: все максимальные – на минимальные.
# 8
# 5 4 2 2 4 2 2 5

'''def max_to_min(list):
    Min = min(list)
    MAx = max(list)
    return [ Min if i == MAx else i for i in list ]
print(*max_to_min([int(i) for i in input().split()]))'''

# Напишите функцию, которая принимает
# одно число и проверяет, является ли оно простым
#
# Напоминание: Простое число - это число,
# которое имеет 2 делителя: 1 и n(само число)

# https://www.delftstack.com/ru/howto/python/python-isprime/
# https://habr.com/ru/post/526924/

'''
def is_prime_number(n):
    if n == 2:
        return True
    elif n == 1 or n % 2 == 0:
        return False
    for i in range(3, int((n ** 0.5) + 1), 2):
        if (n % i == 0):
            return False
    return True


print(is_prime_number(int(input())))
'''

# Дано натуральное число N и последовательность
# из N элементов. Требуется вывести эту
# последовательность в обратном порядке.

# Примечание. В программе запрещается
# объявлять массивы и использовать
# циклы (даже для ввода и вывода).

# def rev_num(num):
#     if num == 0:
#         return ""
#     nums = input()
#     return rev_num(num - 1) + f"{nums} "


# print(rev_num(int(input())))


a = [3, 4, 5, 2, 7, 8]
b = [7, 9, 2, 4, 5, 1]
c = [5, 7, 3, 4, 5, 9]

dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]

dict_b = [{"name": "John", "age": 12},
          {"name": "Sonia", "age": 10},
          {"name": "Steven", "age": 13},
          {"name": "Natasha", "age": 9}]

names = ["Abram", "Arib", "Bob", "Shawn",
         "Aria", "Cicilia", "John", "Reema",
         "Alice", "Craig", "Aaron", "Simi"]