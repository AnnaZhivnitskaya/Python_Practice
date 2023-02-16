# num = {k: v ** 3 for k, v in zip("ASDFGHJK", range(1, 11))}

# print(num)

# Задача 1

# Дан список чисел. Определите,
# сколько в нем встречается различных чисел.

# list_nums = [1, 2, 3, 1, 1, 5, 10, 20, 20, 30]
# print(len(set(list_nums)))


# Задача 2

# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо,
# K – положительное число.
import os

os.system('cls')

# n = int(input('Введите количество элементов: '))
# list_1 = list()
# for i in list_1:
#     a = int(input)
#     list_1.append(a)
# print(*list_1)

list_1 = [1, 2, 3, 4, 5, 6]
num = int(input('Введите шаг сдвига: '))
temp = 0
i = 1 #если положит единица, то сдвиг вправо,
            # если -1, то сдвиг влево
while i <= num:
    temp = list_1.pop()
    list_1.insert(0, temp)
    i +=1
print(list_1)


# решение 1
# list_nums = [1, 2, 3, 4, 5]
# k = 7
# print(list_nums)
# result = list_nums[(k % len(list_nums)):] + list_nums[:(k % len(list_nums))]
# print(result)

# решение 2
# list_nums = [1, 2, 3, 4, 5]
# k = 7

# print(list_nums)

# for i in range(k - 1):
#     list_nums.insert(0, list_nums.pop(- 1))

# print(k, list_nums)


# Напишите программу для печати всех уникальных значений в словаре

# list_dict = [{"V": "S001"}, {"V": "S002"},
#              {"VI": "S001"}, {"VI": "S005"},
#              {"VII": " S005 "}, {"V": " S009 "},
#              {"VIII": " S007 "}]
# print(set( list( i.values())[0].strip() for i in list_dict)) #При преобразовании через List теряем ключи

#Задача 4
# Дан массив, состоящий из целых чисел.
# Напишите программу, которая подсчитает
# количество элементов массива, больших
# предыдущего (элемента с предыдущим номером)
# list_nums = [0, -1, 5, 2, 3]

# print (sum([1 for i in range(1, len(list_nums)) if list_nums[i]>list_nums[i-1]]))