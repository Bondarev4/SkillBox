n = int(input('Кол-во клеток: '))
a = []
for i in range(n):
    print('Эффективность', i, 'клетки:', end = ' ')
    effect = int(input())
    if effect < i:
        a.append(effect)
print('Неподходящие значения:', *a)
