import random
def exchange(arr, count_zero):
    n = len(arr)
    for _ in range(count_zero):
        i = arr.index(0)
        while i < n - 1 or arr[i] != 0:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            i += 1


n = int(input('Введите кол-во эл-ов массива: '))
a = [random.randint(0, 6) for _ in range(n)]
print('\nНачальный список:', a)
counter = a.count(0)
exchange(a, counter)
print('Список с переставленными нулями:', a)
print('Сжатый список:', a[:n - counter])
