def series_of_number(x, number):
    if x > number:
        return x
    print(x)
    return series_of_number(x + 1, number)


n = int(input('Введите num: '))
series_of_number(1, n)
