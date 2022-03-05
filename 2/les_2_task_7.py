"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+number = number(number+1)/2,
 где number - любое натуральное число.
"""

quantity = int(input("Введите натуральное число - количество элементов: "))


def verification(value):
    summa = 0
    for i in range(1, value + 1):
        summa += i
    expression = int(value * (value + 1) / 2)
    if summa == expression:
        print(f'{summa} == {expression} Предположение верно')
    else:
        print(f'{summa} != {expression} Предположение не верно')


verification(quantity)
