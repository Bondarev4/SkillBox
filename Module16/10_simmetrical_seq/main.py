def pal(ar):
    for i in range(len(ar) // 2):
        if ar[i] != ar[-1 - i]:
            return False
    return True
def check(a):
    a1 = a
    counter = 0
    arr = []
    while not pal(a1):
        a1 = []
        counter += 1
        arr.insert(0, a[counter - 1])
        a1.extend(a)
        a1.extend(arr)
    return counter, arr


n = int(input('Кол-во чисел: '))
a = [int(x) for x in input('Введите последовательность чисел: ').split()]
print('\nПоследовательность:', *a)
count, array = check(a)
print('Нужно приписать чисел:', count)
print('Сами числа:', * array)