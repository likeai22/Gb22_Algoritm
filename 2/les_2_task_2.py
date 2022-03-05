"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""

digit = int(input('Введите натуральное число: '))
report_value = digit


# Решение циклом
def odd_even_loop(value, even=0, odd=0):
    while value:
        dig = value % 10
        value = value // 10
        if dig % 2 != 0:
            odd += 1
        else:
            even += 1
    return report(report_value, even, odd)


# Решение рекурсией
def odd_even_recursive(value, even=0, odd=0):
    i = value % 10
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
    if value // 10 == 0:
        return report(report_value, even, odd)
    odd_even_recursive(int(value // 10), even, odd)


def report(data, even, odd):
    print(f'В числе {data}: {even} четных чисел и {odd} нечетных чисел.')


print('\nРешение циклом:')
odd_even_loop(digit)
print('\nРешение рекурсией:')
odd_even_recursive(digit)
