# 1.	В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

numbers = [item for item in range(2, 100)]
dividers = {item for item in range(2, 10)}
numbers_list = []

for item in dividers:
    [numbers_list.append(digit) for digit in numbers if digit % item == 0]
    print(f'{item} кратны - {len(numbers_list)} чисел {numbers_list}.')
    numbers_list.clear()
