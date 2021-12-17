n = int(input('Сколько записей вносится в протокол? '))
records = {}
print('Записи (результат и имя):')
for i in range(1, n + 1):
    score, name = input(' '.join([str(i), 'запись: '])).split()
    if int(score) in records:
        records[int(score)].append(name)
    else:
        records[int(score)] = [name]
print('\nИтоги соревнований:')
place = 1
for score in sorted(records)[::-1]:
    for nick in records[score]:
        print('{} место. {} ({})'.format(place, nick, score))
        place += 1