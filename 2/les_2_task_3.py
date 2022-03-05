"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""

digit = int(input('Введите натуральное число: '))


def reverse_loop(value):
    report_value = ''
    while value != 0:
        report_value += str(value % 10)
        value = value // 10
    return report_value


def reverse_recursive(value):
    report_value = str(value % 10)
    if value // 10 == 0:
        return report_value
    else:
        return report_value + reverse_recursive(value // 10)


print(f'\nРешение циклом: {reverse_loop(digit)}')
print(f'\nРешение рекурсией: {reverse_recursive(digit)}')
