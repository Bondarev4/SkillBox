import math
def count_number(x):
    count = 0
    while x > 0:
        count += 1
        x //= 10
    return count

def sum_number(x):
    sum_n = 0
    while x > 0:
        sum_n += x % 10
        x //= 10
    return sum_n

N = int(input('Введите число: '))
cn = count_number(N)
sn = sum_number(N)
print('Сумма цифр:', sn)
print('Кол-во цифр в числе:', cn)
print('Разность суммы и кол-ва цифр:', abs(cn - sn))