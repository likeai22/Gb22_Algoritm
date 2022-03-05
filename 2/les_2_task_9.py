"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""

number = int(input("Введите число (0 конец): "))
max_num = 0
max_sum = 0

while number != 0:
    sum = 0
    num = number
    while number > 0:
        remainder = number % 10  # Получение остатка от деления числа number на 10
        number //= 10  # Целочисленное деление двух чисел
        sum += remainder  # Сумма цифр
    if sum > max_sum:
        max_sum = sum
        max_num = num

    number = int(input("Введите число: "))
else:
    print(f"Максимальное число - {max_num}, сумма цифр - {max_sum}")
