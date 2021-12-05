c_stick = int(input('Кол-во палок: '))
c_cast = int(input('Кол-во бросков: '))
sticks = list('I' * c_stick)
for i in range(1, c_cast + 1):
    print('\nБросок ' + str(i) + '.', end = ' ')
    l = int(input('Сбиты палки с номера '))
    r = int(input('по номер '))
    sticks[l - 1:r] = ['.' for _ in range(r - l + 1)]
print('Результат', end = ' ')
for x in sticks:
    print(x, end = '')