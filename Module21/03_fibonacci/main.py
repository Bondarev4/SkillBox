def f_num(pos, f=1, s=1):
    if pos == 1:
        return f + s
    return f_num(pos - 1, s, f + s)


num_pos = int(input('Введите позицию числа в ряде Фибоначчи: '))
if num_pos < 3:
    print(1)
else:
    print('\nЧисло: {}'.format(f_num(num_pos - 2)))
