class QHofstadter(object):
    def __init__(self, lst):
        self.lst = lst[:]

    def __next__(self):
        s = self.lst[-self.lst[-1]] + self.lst[-self.lst[-2]]
        self.lst.append(s)
        return s

    def __iter__(self):
        return self


a, b = map(int, input('Введите 2 числа: ').split())
if a == 1 and b == 2:
    print('Немедленная остановка!')
    exit()
elif a < 0 and b < 0:
    print('Ошибка ввода!')
    exit()
q = QHofstadter([a, b])
row = [next(q) for _ in range(25)]
print(*row)
