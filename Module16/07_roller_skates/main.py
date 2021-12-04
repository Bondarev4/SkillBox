count_skates = int(input('Кол-во коньков: '))
skates = []
for i in range(1, count_skates + 1):
    print('Размер', i, 'пары:', end = ' ')
    size = int(input())
    skates.append(size)
count_men = int(input('\nКол-во людей: '))
have_skates = 0
for i in range(1, count_men + 1):
    print('Размер ноги', i, 'человека:', end = ' ')
    size = int(input())
    if skates.count(size) > 0:
        have_skates += 1
        skates.remove(size)
print('Наибольшее кол-во людей, которые могут взять ролики:', have_skates)


