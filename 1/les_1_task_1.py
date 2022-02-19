# 1. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
import operator

x1 = 5
x2 = 6
bin_x1 = f'{x1:08_b}'
bin_x2 = f'{x2:08_b}'
print(x1, bin_x1, ',', x2, bin_x2)  # 5 0b101 , 6 0b110

# Битовое отрицание (NOT)
negation_x1 = ~x1
negation_x2 = ~x2
negation_bin_x1 = bin((1 << 8) - negation_x1)
negation_bin_x2 = bin((1 << 8) - negation_x2)
print(negation_x1, negation_bin_x1, ',', negation_x2, negation_bin_x2)  # -6 0b100000110 , -7 0b100000111

# Коньюкция
conjunction_1 = x1 & x2
conjunction_2 = x2 & x1
print(conjunction_1, conjunction_2)  # коммутативность

# Дизъюнкция
disjunction_1 = x1 | x2
disjunction_2 = x2 | x1
print(disjunction_1, disjunction_2)  # коммутативность

# Исключающее или
exclusive_disjunction_1 = x1 ^ x2
exclusive_disjunction_2 = operator.xor(x1, x2)
print(exclusive_disjunction_1, exclusive_disjunction_2)  # коммутативность

# битовый сдвиг
circular_shift_1 = x1 >> 2  # 101 --> 10100 сдвиг вправо >> (целочисленное деление на 2)
circular_shift_2 = x1 << 2  # 101 --> 1 сдвиг влево << (умножение на 2)
print(f'{circular_shift_1:08_b}', f'{circular_shift_2:08_b}')

