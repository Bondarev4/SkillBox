a = [int(x) for x in input('Первый список: ').split()]
b = [int(x) for x in input('Второй список: ').split()]
a.extend(b)
i = 0
while i < len(a):
    count = a.count(a[i])
    for j in range(count - 1):
        a.remove(a[i])
    i += 1

print('Новый первый список с уникальными элементами:', a)
