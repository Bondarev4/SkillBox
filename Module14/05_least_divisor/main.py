def min_devider(x):
    dev = 0
    for number in range(2, x + 1):
        if x % number == 0:
            dev = number
            break
    return dev

x = int(input('Введите число: '))
print('Наименьший делитель, отличный от единицы:', min_devider(x))
