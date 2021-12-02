def sort(a):
    j = 1
    n = len(a)
    while j < n:
        for i in range(n - j):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
        j += 1

first_class = list(range(160, 177, 2))
second_class = list(range(162, 181, 3))
first_class.extend(second_class)
sort(first_class)
print(first_class)

