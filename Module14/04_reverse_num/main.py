def reversre_int(x):
    x = int(x)
    d = 0
    while x > 0:
        d = d * 10 + x % 10
        x //= 10
    return d
def reversre_float(x):
    d = 0
    while int(x) < x:
        x *= 10
        d = d / 10 + int(x) % 10
    d /= 10
    return d

a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
a_r = reversre_int(a) + reversre_float(a)
b_r = reversre_int(b) + reversre_float(b)
print('\nПервое число наоборот:', a_r, '\nВторое число наоборот', b_r)
print('Сумма:', a_r + b_r)

