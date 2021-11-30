list = [int(x) for x in input('Изначальный список: ').split()]
k = int(input('Сдвиг: '))
n = len(list)
k %= n
list1 = [0] * n
for i in range(n):
    list1[(i + k) % n] = list[i]
print('Сдвинутый список: ', list1)