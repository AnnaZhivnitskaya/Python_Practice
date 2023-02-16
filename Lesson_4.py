'''Задача №25. Решение в группах 

Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ 
уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n. 

Input: a a a b c a a d c d d 
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2 

Для решения данной задачи используйте функцию .split()'''

# string = input().split()

# for i in range(len(string)):
#     count = 1
#     for j in range(i + 1, len(string)):
#         if string[i] == string[j]:
#             string[j] += "_" + str(count)
#             count += 1
    

# print(string)

# Условный (тернарный) оператор -  оператор , принимающий три операнда: условие, , 
# затем выражение, которое выполняется, если условие истинно, и, 
# выражение, которое выполняется, если условие ложно.

'''
Задача №27. Общее обсуждение 

Пользователь вводит текст(строка). 
ловом считается последовательность непробельных символов идущих подряд, слова разделены одним 
или большим числом пробелов или символами конца строки.

Определите, сколько различных слов содержится в этом тексте. 

Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure
So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells 
Output: 19
'''
# string = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
# string = set(string.lower().split())
# print(len(string))

#Ремонт кода
n = int(input())
max_number = 0
while n > 0:
    
    if max_number < n:
        max_number = n
n = int(input())   
print(max_number)


# n = int(input())
# max_number = -1
# while n > 0:
#     if max_number < n:
#         max_number = n 
#         n = int(input())
# print(max_number)


'''n = int(input())
max_number = 0
while n != 0:
    n = int(input())
    if max_number < n:
        max_number = n
print(max_number)

n = int(input())
max_number = -1
while n > 0:    
    if max_number < n:
       max_number = n
    n = int(input())
print(max_number)'''