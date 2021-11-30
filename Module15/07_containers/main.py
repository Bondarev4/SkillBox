n = int(input('Кол-во контейнеров: '))
boxes = []
for i in range(n):
    x = int(input('Введите вес контейнера: '))
    boxes.append(x)
x = int(input('\nВведите вес нового контейнера: '))
spot = -1
for i in range(n):
    if boxes[i] < x:
        spot = i + 1
        break
if spot == -1:
    print('Номер, куда встанет новый контейнер:', n + 1)
else:
    print('Номер, куда встанет новый контейнер:', spot)

