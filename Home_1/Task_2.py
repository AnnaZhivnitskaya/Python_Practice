# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа 
# сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, 
# чем Петя и Сережа вместе?

sum = int(input("Введите количество журавликов: "))
p = int(sum / 4)
k = int(sum / 2)

if sum % 4 != 0:
    print("Решение некорректно")
else:
    print(f"Петя и Сережа сделали по {p} журавликов, Катя сделала {k} журавликов")