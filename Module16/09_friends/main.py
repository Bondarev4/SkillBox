n = int(input('Кол-во друзей: '))
k = int(input('Долговых расписок: '))
friends = [0] * n
for i in range(k):
    print()
    print(i + 1, 'расписка')
    to = int(input('Кому: '))
    who = int(input('От кого: '))
    money = int(input('Сколько: '))
    friends[to - 1] -= money
    friends[who - 1] += money
print('\nБаланс друзей:')
for i in range(n):
    print(i + 1, ':', friends[i])