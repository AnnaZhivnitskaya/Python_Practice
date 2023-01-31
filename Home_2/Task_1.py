'''На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были 
повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть.'''

import os

os.system('cls')
n = int(input("Введите количество монет: "))

count_0 = 0
count_1 = 0
for i in range(n):
    i = int(input())
    if i == 0:
        count_0 += 1
    else:
        count_1 += 1

if count_0 < n / 2:
    print(f'Переверните {count_0} монеты')
else:
    print(f'Переверните {count_1} монеты')