"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления, задача решается в несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит. Поэтому использование встроенных функций для перевода из одной системы счисления в другую в данной задаче под запретом.
"""

from collections import deque, OrderedDict


def hex_dec(hex_num):
    hx_lst = deque(hex_num)
    hx_lst.reverse()
    power, answer = 1, 0
    for i in hx_lst:
        if i < 'A':
            answer += int(i) * power
        else:
            answer += (ord(i) - ord('A') + 10) * power
        power *= 16
    return answer


# решаем переводом в десятичные и обратно, не используя hex() и/или int()
def dec_hex(dec_num):
    lst = []
    int_num = OrderedDict()
    lst_let = '0123456789ABCDEF'
    for key, value in enumerate(lst_let):
        int_num[key] = value

    while dec_num > 0:
        lst.append(dec_num % 16)
        dec_num //= 16

    return [int_num[i] for i in lst[::-1]]


## без перевода
def hex_sum(lst1, lst2):
    hex_sym = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
    lst2.reverse()
    lst_sum = deque([])
    j, k = -1, 0
    for i in lst2:
        ls_temp1 = hex_sym.index(i)
        ls_temp2 = hex_sym.index(lst1[j])
        lst_sum.appendleft(hex_sym[(ls_temp1 + ls_temp2 + k) % 16])
        if (ls_temp1 + ls_temp2) >= 15:
            k = 1
        else:
            k = 0
        j -= 1
        if j == -len(lst1) - 1:
            break
    diff = len(lst2) - len(lst1)
    if diff:
        for i in lst2[-diff]:
            lst_sum.appendleft(hex_sym[(hex_sym.index(lst2[-diff]) + k) % 16])
            if hex_sym.index(lst2[-diff]) + 1 >= 15:
                k = 1
            else:
                k = 0
    if k == 1:
        lst_sum.appendleft('1')
    return list(lst_sum)


lst_1 = deque([i for i in input('Введите первое число: ').upper()])
lst_2 = deque([i for i in input('Введите второе число: ').upper()])

print('Сумма чисел равна: ', hex_sum(lst_1, lst_2))

num1 = list(input('Введите первое шестнадцатиричное число: ').upper())
num2 = list(input('Введите второе шестнадцатиричное число: ').upper())

print('Первое 16-e число: ', num1)
print('Второе 16-e число: ', num2)

num1_dec = hex_dec(num1)
num2_dec = hex_dec(num2)

print('Сумма чисел равна: ', dec_hex(num1_dec + num2_dec))
print('Произведение чисел равно: ', dec_hex(num1_dec * num2_dec))

"""
Введите первое шестнадцатиричное число: a2
Введите второе шестнадцатиричное число: c4f
Первое 16-e число:  ['A', '2']
Второе 16-e число:  ['C', '4', 'F']
Сумма чисел равна:  ['C', 'F', '1']
Произведение чисел равно:  ['7', 'C', '9', 'F', 'E']
"""
