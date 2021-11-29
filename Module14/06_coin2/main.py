def around(x, y, r):
    if x ** 2 + y ** 2 <= r:
        return True
    return False

x = float(input('Введите координаты монетки:\nX: '))
y = float(input('Y: '))
r = int(input('Введите радиус: '))
if around(x, y, r):
    print('Монетка где-то рядом')
else:
    print('Монетки в области нет')