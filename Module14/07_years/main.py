def simil_number(x, number):
    k = 0
    while x > 0:
        if x % 10 == number:
            k += 1
        x //= 10
    return k == 3

def simil_num_3(x):
    while x > 0:
        d = x % 10
        if simil_number(x, d):
            return True
        x //= 10
    return False

start = int(input('Введите первый год: '))
stop = int(input('Введите второй год: '))
print('Года от', start, 'до', stop, 'с тремя одинаковыми цифрами:')
for year in range(start, stop + 1):
    if simil_num_3(year):
        print(year)