'''Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.'''
import os

os.system('cls')

a = int(input())
b = int(input())

def sum(a, b):
    if not b:
        return a
    a += 1
    b -= 1
    return (sum(a, b))

print(sum(a, b))
    