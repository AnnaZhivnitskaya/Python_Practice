'''
3 настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским алфавитом очки распределяются так:

● A, E, I, O, U, L, N, S, T, R – 1 очко;
● D, G – 2 очка;
● B, C, M, P – 3 очка;
● F, H, V, W, Y – 4 очка;
● K – 5 очков;
● J, X – 8 очков;
● Q, Z – 10 очков.

А русские буквы оцениваются так:
● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
● Д, К, Л, М, П, У – 2 очка;
● Б, Г, Ё, Ь, Я – 3 очка;
● Й, Ы – 4 очка;
● Ж, З, Х, Ц, Ч – 5 очков;
● Ш, Э, Ю – 8 очков;
● Ф, Щ, Ъ – 10 очков.

Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что 
на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

*Пример:*
Ввод:
ноутбук
Вывод:
12
'''

scrabble_dict = {1: 'AEIOULNSTRАВЕИНОРСТ',
                 2: 'DGДКЛМПУ',
                 3: 'BCMPБГЁЬЯ',
                 4: 'FHVWYЙЫ',
                 5: 'KЖЗХЦЧ',
                 8: 'JXШЭЮ',
                 10: 'QZФЩЪ'}
word = input('Введите слово: ').upper()
# k - ключ,
# v - значение

print(sum([k for i in word for (k, v) in scrabble_dict.items() if i in v]))
# <название словаря>.items() - метод возвращает итерируемую пару "ключ-значение"
# метод исп-ся, когда надо перебрать значения словаря.
# Позволяет обращаться к ключам и значениям одновременно – если очередная буква в слове входит в одно из значений, 
# генератор добавит ключ в список, а метод списка sum() подсчитает стоимость всего слова
