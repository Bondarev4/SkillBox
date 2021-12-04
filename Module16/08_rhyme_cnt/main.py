count_p = int(input('Кол-во человек: '))
number = int(input('Какое число в считалке? '))
players = list(range(1, count_p + 1))
print('Значит, выбывает каждый', number, 'человек')
start_i = 0
while len(players) > 1:
    print('\nТекущий круг людей:', players)
    print('Начало счёта с номера', players[start_i % len(players)])
    start_i = (start_i + number - 1) % len(players)
    print('Выбывает человек под номером', players[start_i])
    players.remove(players[start_i])
print('\nОстался человек под номером', players[0])