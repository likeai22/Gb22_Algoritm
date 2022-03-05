"""
5.	Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""


letter_number_start = 32
letter_number_end = 128
length = 10

for i in range(letter_number_start, letter_number_end):
    print('%6d-%s' % (i, chr(i)), end='')
    if (i - letter_number_start + 1) % length == 0:
        print('')
