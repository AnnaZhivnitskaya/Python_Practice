'''Напишите программу, которая на вход принимает два числа A и B, 
и возводит число А в целую степень B с помощью рекурсии.'''
import os

os.system("cls")

a = int(input())
b = int(input())
def result(a, b):
    if b == 0:
        return 1
    return a * result(a, (b - 1))
    
print(result(a, b))