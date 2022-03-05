"""
4.	Найти сумму number элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (number) вводится с клавиатуры.
"""

quantity = int(input("Введите количество элементов ряда: "))

"""
по формуле для геометрической прогрессии:
q = -0.5 / 1 = -0.5
b_n = q ** (number - 1)
s_n = b_1 * (q ** number - 1) / (q - 1))
"""


def geom_progression(value):
    x = 1
    s = 0
    for i in range(value):
        s += x
        x /= -2
    return s


def geom_progression_recursive(value):
    b1 = 1
    q = -0.5
    if value == 1:
        return b1
    else:
        return b1 + geom_progression_recursive(value - 1) * q


print(f'\nСумма циклом: {geom_progression(quantity)}')
print(f'\nСумма рекурсией: {geom_progression_recursive(quantity)}')
