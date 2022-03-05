'''
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.
'''


quantity = int(input('Количество чисел: '))
riddle_number = int(input('Искомая цифра: '))

qnt_riddle_number = 0

for item in range(quantity):
    value = int(input(f'Введите цифру № {item + 1} '))
    if value == riddle_number:
        item += 1
        qnt_riddle_number += 1
    else:
        item += 1
print(f'Искомая цифра встречалась {qnt_riddle_number} раз(а)')
