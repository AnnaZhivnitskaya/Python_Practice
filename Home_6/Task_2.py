'''Определить индексы элементов массива (списка), 
значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)
Ввод:  -5 9 0 3 -1 -2 1 4 -2 10 2 0 -9 8 10 -9 0 -5 -5 7
min 5
max 15
Вывод: [1, 9, 13, 14, 19]
'''
import os

os.system('cls')

arr = list(map(int,input().split())) # 2 3 -9 12 -7 0 65 8 -2 -14 10 14 -3 11 -10 0 -5 5 12 -12 1 13
print(arr)
mini = int(input())
maxi = int(input())
change = []
for i in range(len(arr)-1): 
    if maxi >= arr[i] >= mini:
        change.append(i)
print(change)

print(change)