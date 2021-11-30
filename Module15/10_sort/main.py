a = [int(x) for x in input('Введите список: ').split()]
j = 1
n = len(a)
while j < n:
   for i in range(n - j):
       if a[i] > a[i + 1]:
           a[i], a[i + 1] = a[i + 1], a[i]
   j += 1
print('Отсортированный список:', *a)