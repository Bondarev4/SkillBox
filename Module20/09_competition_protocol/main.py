n = int(input('Сколько записей вносится в протокол? '))
records = {}
print('Записи (результат и имя):')
for i in range(1, n + 1):
    score, name = input(' '.join([str(i), 'запись: '])).split()
    if score in records:
        records[int(score)] += name
    else:
        records[int(score)] = [name]
print('\nИтоги соревнований:')
place = 1
for score in sorted(records):
    k = len(records[score])
    if k > 1:
        for el in records[score]:
            print('{} место.'.format(place), score, *records[score])
            place += 1
    else:
        print('{} место.'.format(place), score, *records[score])
        place += 1